from rest_framework import serializers
from django.contrib.auth import get_user_model
from cinema.models import Movie

User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title_english', 'actors', 'genres', 'year', 'rating', 'runtime', 'medium_cover_image')
