from django.contrib import admin
from .models import User, CinemaAdmin, CinemaGoer, CinemaGoerAdd

admin.site.register(User)
admin.site.register(CinemaGoer)
admin.site.register(CinemaGoerAdd)
admin.site.register(CinemaAdmin)

