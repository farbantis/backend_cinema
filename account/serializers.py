from djoser.serializers import UserCreateSerializer
from account.models import CinemaUser


class CinemaUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CinemaUser
        fields = ('id', 'email', 'password')
