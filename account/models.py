from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static
from validators import validate_file_size, upload_path_and_rename
from .managers import CinemaUserManager


class CinemaUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CinemaUserManager()

    def __str__(self):
        return self.email


# add - likes, comment, profile (collect data about user ? cookies?)
class Cinemagoer(CinemaUser):
    class CinemagoerStatusLimits:
        """sets the amount to update the status level e.g. if amount of purchase more 1000, status is Silver"""
        BRONZE = 1_000
        SILVER = 10_000
        GOLD = 100_000
        PLATINUM = 1_000_000  # we believe it's impossible for user to reach this amount
        cinemagoer_status_limits = ('BRONZE', BRONZE), ('SILVER', SILVER), ('GOLD', GOLD), ('PLATINUM', PLATINUM)

    class CinemagoerStatus(models.TextChoices):
        BRONZE = 'BRONZE', 'BRONZE'
        SILVER = 'SILVER', 'SILVER'
        GOLD = 'GOLD', 'GOLD'
        PLATINUM = 'PLATINUM', 'PLATINUM'

    class CinemagoerGender(models.TextChoices):
        MALE = 'M', 'MALE'
        FEMALE = 'F', 'FEMALE'
        NO_DATA = 'N', '-'

    picture = models.ImageField(upload_to=upload_path_and_rename,
                                blank=True, null=True,
                                validators=[validate_image_file_extension, validate_file_size])

    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=CinemagoerGender.choices, default=CinemagoerGender.NO_DATA)
    status = models.CharField(max_length=15, choices=CinemagoerStatus.choices, default=CinemagoerStatus.BRONZE)
    is_active_cinema_goer = models.BooleanField(default=True)
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
        lst_of_status_names = [x[0] for x in Cinemagoer.CinemagoerStatusLimits.cinemagoer_status_limits]
        previous_status = self.status
        # getting current status
        for st in Cinemagoer.CinemagoerStatusLimits.cinemagoer_status_limits:
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
