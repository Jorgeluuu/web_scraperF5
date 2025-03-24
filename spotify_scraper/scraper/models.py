from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    playlist_title = models.CharField(max_length=200)
    song_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return self.title