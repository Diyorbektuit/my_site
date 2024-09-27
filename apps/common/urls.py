from django.urls import path
from apps.common import views

urlpatterns = [
    path('post-create/', views.PostCreateView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('register/', views.UserRegisterView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('users-list/', views.UsersListForAdmin.as_view()),
    path('create-superuser/', views.RegisterSuperUser.as_view())
]