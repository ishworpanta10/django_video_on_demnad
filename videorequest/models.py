from django.db import models
from django.utils import timezone

# Create your models here.


class Video(models.Model):
    videotitle = models.CharField(max_length=50)
    videodesc = models.TextField()
    date_added = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return "Name: {}, ID: {}".format(self.videotitle, self.id)
