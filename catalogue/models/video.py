from django.db import models
from .show import *

# Create your models here.
class Video(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="ID_video")
    title = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255, unique=True)
    show = models.ForeignKey(Show, on_delete=models.PROTECT, null=True, verbose_name="ID_show")


    class Meta:
        db_table = "videos"

    def __str__(self):
        return self.title