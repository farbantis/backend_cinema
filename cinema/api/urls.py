from django.urls import path
from cinema.api.resources import MoviesAPIView

urlpatterns = [
    path('movies/', MoviesAPIView.as_view()),
]