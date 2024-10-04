from rest_framework import serializers
from .models import User

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'role',
            'password'
        )