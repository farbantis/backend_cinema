from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import User, Movie


# User = get_user_model()


# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'username', 'password', 'email')


# class UserRegistrSerializer(serializers.ModelSerializer):
#     # Поле для повторения пароля
#     password2 = serializers.CharField()
#
#     # Настройка полей
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password', 'password2']
#
#     # Метод для сохранения нового пользователя
#     def save(self, *args, **kwargs):
#         # Создаём объект класса User
#         user = User(email=self.validated_data['email'], username=self.validated_data['username'], )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password != password2:
#             raise serializers.ValidationError({password: "Пароль не совпадает"})
#         user.set_password(password)
#         user.save()
#         return user


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'title_english', 'actors', 'genres', 'year', 'rating', 'runtime', 'medium_cover_image')
