from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from cinema.api.serializers import MovieSerializer
from cinema.models import Movie


class MovieSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'


class MoviesAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MovieSetPagination
