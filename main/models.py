from django.contrib.auth.models import update_last_login
from django.db.models.fields import DateTimeField
from gag.minix import TranslateMixin
from django.db import models
from gag.helpers import UploadTo
from client.models import User
from django.utils.translation import gettext_lazy as _
import os

class Category(TranslateMixin, models.Model):
    translate_fields = ['name']

    name_uz = models.CharField(max_length=50, verbose_name="Nomi (uz)")
    name_ru = models.CharField(max_length=50, verbose_name="Nomi (ru)")
    image = models.ImageField(upload_to=UploadTo("category"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Post(TranslateMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, default=None, null=True)
    comment = models.TextField(verbose_name=_("Izoh"))
    file = models.FileField(verbose_name=_("Rasm/Video"), upload_to=UploadTo("post"))
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def ext(self):
        return(os.path.splitext(self.file.name)[1])[1:].lower()

    @property
    def is_image(self):
        return self.ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']
    
    @property
    def is_video(self):
        return self.ext in ['mp4', 'mpeg']

    @property
    def is_audio(self):
        return self.ext in ['mp3', 'wav']


class PostComment(TranslateMixin, models.Model):
    parent = models.ForeignKey("PostComment", on_delete=models.RESTRICT, null=True, default=None, related_name="PostComment")
    post = models.ForeignKey(Post, on_delete=models.RESTRICT, default='username')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default='username')
    comment = models.TextField(verbose_name=_("Izoh"))
    image = models.ImageField(upload_to=UploadTo("comment"), null=True, blank=True, default=None)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)