from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .serializer import PostCreateSerializer, PostListSerializer, UsersListSerializer
from .models import Post, User
from rest_framework.views import APIView, Response, status
from .permissions import IsAdminPermission
from rest_framework.permissions import AllowAny


class UserRegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        username = self.request.data.get('username')
        password1 = self.request.data.get('password1')
        password2 = self.request.data.get('password2')

        if password1 is None or password2 is None:
            raise ValidationError(
                detail={
                    'msg': "parol kiritilishi shart"
                }
            )
        if username is None:
            raise ValidationError(
                detail={
                    'msg': "username kiritilishi shart"
                }
            )
        if password1 != password2:
            raise ValidationError(
                detail={
                    'msg': "parollar mos emas"
                }
            )

        try:
            user = User.objects.get(username=username)
            raise ValidationError(detail={
                'msg': "Bu usernameli user allaqachon mavjud"
            })
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username,
                password=password1
            )

            response_data = {
                'username': username,
                'access_token': user.tokens().get('access') ,
                "refresh_token": user.tokens().get('refresh')
            }

            return Response(response_data, status=status.HTTP_200_OK)


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        username = self.request.data.get('username')
        password = self.request.data.get('password')

        if username is None:
            raise ValidationError(
                detail={
                    'msg': "username kiritilishi shart"
                }
            )
        if password is None:
            raise ValidationError(
                detail={
                    'msg': "parol kiritilishi shart"
                }
            )


        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                response_data = {
                    'username': username,
                    'access_token': user.tokens().get('access'),
                    "refresh_token": user.tokens().get('refresh')
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                raise ValidationError(
                    detail={
                        'msg': "parol notog'ri kiritildi boshqattan urinib ko'ring"
                    }
                )
        except User.DoesNotExist:
            raise ValidationError(
                detail={
                    'msg': "username xato kiritildi yoki siz hali ro'yhatdan o'tmagansiz"
                }
            )

class RegisterSuperUser(APIView):
    permission_classes = (AllowAny, )

    def post(self, *args, **kwargs):
        username = self.request.data.get('username')
        password1 = self.request.data.get('password1')
        password2 = self.request.data.get('password2')

        if password1 is None or password2 is None:
            raise ValidationError(
                detail={
                    'msg': "parol kiritilishi shart"
                }
            )
        if username is None:
            raise ValidationError(
                detail={
                    'msg': "username kiritilishi shart"
                }
            )
        if password1 != password2:
            raise ValidationError(
                detail={
                    'msg': "parollar mos emas"
                }
            )

        try:
            user = User.objects.get(username=username)
            raise ValidationError(detail={
                'msg': "Bu usernameli user allaqachon mavjud"
            })
        except User.DoesNotExist:
            user = User.objects.create_superuser(
                username=username,
                password=password1
            )

            response_data = {
                'username': username,
                'access_token': user.tokens().get('access') ,
                "refresh_token": user.tokens().get('refresh')
            }

            return Response(response_data, status=status.HTTP_200_OK)


class UsersListForAdmin(generics.ListAPIView):
    # permission_classes = (IsAdminPermission, )
    serializer_class = UsersListSerializer

    def get_queryset(self):
        print(111)
        user = self.request.user
        print(user)
        if user.is_superuser:
            return User.objects.all()
        else:
            return []

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
