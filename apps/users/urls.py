from django.urls import path
from apps.users import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('users-list/', views.UsersListForAdmin.as_view()),
    path('create-superuser/', views.RegisterSuperUser.as_view())
]