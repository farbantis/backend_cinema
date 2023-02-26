from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import User

# User = get_user_model()
print(f'user is {User}')


class CinemaUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password')
