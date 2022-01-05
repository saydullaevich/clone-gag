from django.db import models
from django.contrib.auth.models import AbstractUser
from gag.helpers import UploadTo
from django.templatetags.static import static

class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo("profile"))

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url

        return static("img/no_avatar.png")