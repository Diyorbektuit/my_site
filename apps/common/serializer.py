from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'slug'
        )

