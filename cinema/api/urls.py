from django.urls import path
from cinema.api.resources import MoviesAPIView, MovieAPIView, ActorsAPIView, ActorAPIView

urlpatterns = [
    path('movies/', MoviesAPIView.as_view()),
    path('actors/', ActorsAPIView.as_view()),
    path('movie/<int:movie_id>/', MovieAPIView.as_view()),
    path('actor/<int:actor_id>/', ActorAPIView.as_view()),
]
