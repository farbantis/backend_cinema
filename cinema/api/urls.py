from django.urls import path
from cinema.api.resources import MoviesAPIView, MovieAPIView

urlpatterns = [
    path('movies/', MoviesAPIView.as_view()),
    path('movie/<int:movie_id>/', MovieAPIView.as_view()),
]