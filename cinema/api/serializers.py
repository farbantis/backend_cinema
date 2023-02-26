from rest_framework import serializers
from django.contrib.auth import get_user_model
from cinema.models import Movie

User = get_user_model()


class MoviesSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title_english', 'actors', 'genres', 'rating', 'medium_cover_image')


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'