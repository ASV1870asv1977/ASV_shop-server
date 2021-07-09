from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    # В базе все необходимые данные прописаны в соответствии с наследованием
