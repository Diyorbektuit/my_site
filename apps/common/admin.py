from django.contrib import admin
from .models import User, Post
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'is_superuser', 'role')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'created_at')