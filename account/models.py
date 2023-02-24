from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from django.db import models
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from account.validators import validate_file_size, upload_path_and_rename
from .managers import UserManager


class User(AbstractUser):
    class Types(models.TextChoices):
        CINEMA_GOER = 'CG', _('CinemaGoer')
        CINEMA_ADMIN = 'CA', _('CinemaAdmin')
    type = models.CharField(_('user type'), max_length=50, choices=Types.choices, default=Types.CINEMA_GOER)
    email = models.EmailField(_("email address"), unique=True)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.type == self.Types.CINEMA_GOER:
            CinemaGoerAdd.objects.create(user_id=self.id)


class CinemaAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CINEMA_ADMIN)


class CinemaAdmin(User):
    objects = CinemaAdminManager()

    class Meta:
        proxy = True
        verbose_name = 'CinemaAdmin'
        verbose_name_plural = "CinemaAdmins"


class CinemaGoerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CINEMA_GOER)


class CinemaGoer(User):
    objects = CinemaGoerManager()

    class Meta:
        verbose_name = 'CinemaGoer'
        verbose_name_plural = 'CinemaGoers'
        proxy = True


class CinemaGoerAdd(models.Model):

    class CinemaGoerStatusLimits:
        """sets the amount to update the status level e.g. if amount of purchase more 1000, status is Silver"""
        BRONZE = 1_000
        SILVER = 10_000
        GOLD = 100_000
        PLATINUM = 1_000_000  # we believe it's impossible for user to reach this amount
        cinemagoer_status_limits = ('BRONZE', BRONZE), ('SILVER', SILVER), ('GOLD', GOLD), ('PLATINUM', PLATINUM)

    class CinemaGoerStatus(models.TextChoices):
        BRONZE = 'BRONZE', 'BRONZE'
        SILVER = 'SILVER', 'SILVER'
        GOLD = 'GOLD', 'GOLD'
        PLATINUM = 'PLATINUM', 'PLATINUM'

    class CinemaGoerGender(models.TextChoices):
        MALE = 'M', 'MALE'
        FEMALE = 'F', 'FEMALE'
        NO_DATA = 'N', '-'

    user = models.OneToOneField(CinemaGoer, on_delete=models.CASCADE, default=12)
    picture = models.ImageField(upload_to=upload_path_and_rename,
                                blank=True, null=True,
                                validators=[validate_image_file_extension, validate_file_size])
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=CinemaGoerGender.choices, default=CinemaGoerGender.NO_DATA)
    status = models.CharField(max_length=15, choices=CinemaGoerStatus.choices, default=CinemaGoerStatus.BRONZE)
    bonus = models.IntegerField(default=0)
    amount_of_purchase = models.IntegerField(default=0)
    default_pic_mapping = {'N': 'no_data.jpg', 'MALE': 'male.jpg', 'FEMALE': 'female.jpg'}

    @property
    def get_cinemagoer_pic_url(self):
        """if no picture of cinemagoer we should place default one based on gender if any"""
        if not self.picture:
            return static(f'cinema/pictures/default_user/{self.default_pic_mapping[self.gender]}/')
        return self.picture.url

    @property
    def get_cinemagoer_status(self):
        """set the cinemagoer status based on the amount of purchases"""
        # !! а если бы мы хотели подсчитываеть количество изменений статуса.... => записывать кол-во в бд?..
        lst_of_status_names = [x[0] for x in CinemaGoerAdd.CinemaGoerStatusLimits.cinemagoer_status_limits]
        previous_status = self.status
        # getting current status
        for st in CinemaGoerAdd.CinemaGoerStatusLimits.cinemagoer_status_limits:
            if self.amount_of_purchase < st[-1]:
                self.status = st[0]
        #  if status has changed, we have to inform the user by email ?? and in cabinet ??!
        if previous_status != self.status:
            if lst_of_status_names.index(previous_status) < lst_of_status_names.index(self.status):
                action_status = 'going_up'
            else:
                action_status = 'going_down'
            # change_status_notification(self.user, self.status, action_status)
        return self.status


    # @property
    # def get_amount_of_purchase(self):
    #     """returns the amount of purchases within the given time span for status determination"""
    #     # ? how to implement this..... separate table date:purchase amount?
    #     pass
    #
    # def __str__(self):
    #     return f'{self.user}'

