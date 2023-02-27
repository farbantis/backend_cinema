from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from cinema.api.serializers import MoviesSerializer, MovieSerializer, ActorSerializer
from cinema.models import Movie, Actor


class MovieSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'


class MoviesAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    pagination_class = MovieSetPagination


class MovieAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    lookup_url_kwarg = 'movie_id'
    serializer_class = MovieSerializer


class ActorsAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = MovieSetPagination


class ActorAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    lookup_url_kwarg = 'actor_id'
    serializer_class = ActorSerializer

