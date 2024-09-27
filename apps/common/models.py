from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUserManager(UserManager):
    def _create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username,  **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username=username, password=password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(username=username, password=password, **extra_fields)

class User(AbstractUser, BaseModel):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default="user")
    username = models.CharField(max_length=150, unique=True)

    groups = models.ManyToManyField(Group, related_name="common_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="common_user_permissions", blank=True)

    objects = CustomUserManager()

    class Meta:
        db_table = "common_user"  # Unique table name
        verbose_name = "User"
        verbose_name_plural = "Users"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }



class Post(BaseModel):
    title = models.CharField(max_length=123)
    body = RichTextField()
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=123, null=True, blank=True)

    def __str__(self):
        return self.title





