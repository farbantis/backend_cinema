# from django.conf import settings
# from django.db import models
# from django.templatetags.static import static
# from django.urls import reverse
# from django.contrib.auth.models import User
#
#
# # Movie - Genre - Actor - Character
# # Extended User Model - Cinemagoer
# # Cart - tickets (including purchase using bonuses, bonuses for purchases...etc..)
# # free ticket if birthday, discounts on monday morning, and sunday evening
#
#
# class Genre(models.Model):
#     title = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Character(models.Model):
#     name = models.CharField(max_length=250, null=True, blank=True)
#     movie = models.ForeignKey('Movie', on_delete=models.CASCADE)  # movie_id
#     actor = models.ForeignKey('Actor', on_delete=models.CASCADE)  # actor_id
#
#     def __str__(self):
#         return self.name
#
#
# class Actor(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     photo = models.ImageField(null=True, blank=True)
#     imdb_code = models.CharField(max_length=50, null=True, blank=True)
#     genres = models.ManyToManyField(Genre, default='no info')  # new added
#
#     def __str__(self):
#         return self.name
#
#
# class Language(models.Model):
#     language = models.CharField(max_length=20)
#
#
# class Movie(models.Model):
#     genres = models.ManyToManyField(Genre, default='no info')  # new added
#     actors = models.ManyToManyField(Actor, through=Character, default='John')  # new added
#     title_english = models.CharField(max_length=255, null=True, blank=True)
#     code_id = models.IntegerField(null=True, blank=True)
#     imdb_code = models.CharField(max_length=50, null=True, blank=True)
#     slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
#     year = models.PositiveSmallIntegerField(null=True, blank=True)
#     rating = models.FloatField(null=True, blank=True)
#     runtime = models.SmallIntegerField(null=True, blank=True)
#     download_count = models.IntegerField(null=True, blank=True)
#     like_count = models.IntegerField(null=True, blank=True)
#     description_intro = models.TextField(null=True, blank=True)
#     description_full = models.TextField(null=True, blank=True)
#     language = models.CharField(max_length=50, null=True, blank=True)  # MUST be foreignkey for language !!!!
#     lang = models.ForeignKey(Language, blank=True, null=True, on_delete=models.DO_NOTHING)
#     mpa_rating = models.CharField(max_length=10, null=True, blank=True)
#     date_uploaded = models.DateTimeField(null=True, blank=True)
#
#     small_cover_image = models.ImageField(blank=True, null=True)
#     medium_cover_image = models.ImageField(blank=True, null=True)
#     large_cover_image = models.ImageField(blank=True, null=True)
#
#     large_screenshot_image1 = models.ImageField(blank=True, null=True)
#     large_screenshot_image2 = models.ImageField(blank=True, null=True)
#     large_screenshot_image3 = models.ImageField(blank=True, null=True)
#
#     def __str__(self):
#         return self.title_english
#
#     def get_absolute_url(self):
#         return reverse('cinema:index', args=[self.slug])
#
