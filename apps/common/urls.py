from django.urls import path
from apps.common import views

urlpatterns = [
    path('post-create/', views.PostCreateView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
]