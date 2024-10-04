from rest_framework import generics
from .serializer import PostCreateSerializer, PostListSerializer
from .models import Post
from ..users.permissions import IsAdminPermission
from rest_framework.permissions import AllowAny


class PostCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminPermission, )
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        list_title = serializer.validated_data.get('title')
        list_title = list_title.split()
        slug = f""
        for item in list_title:
            slug += f"{item}-"
        post = serializer.save()
        slug += f"{post.id}"
        serializer.save(slug=slug)


class PostListView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(is_active=True)


class PostDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostListSerializer
    queryset = Post.objects.filter(is_active=True)