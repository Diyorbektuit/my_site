from django.db import models
from ..users.models import BaseModel
from ckeditor.fields import RichTextField



class Post(BaseModel):
    title = models.CharField(max_length=123)
    body = RichTextField()
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=123, null=True, blank=True)

    def __str__(self):
        return self.title


class Projects(BaseModel):
    title = models.CharField(max_length=123)
    body = RichTextField()
    image = models.ImageField(upload_to='media/project-images/')
    url = models.CharField(max_length=123)
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=123, null=True, blank=True)

    def __str__(self):
        return self.title



