from django.db import models
from filebrowser.fields import FileBrowseField
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField() # for tinymce
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Media(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='media')
    media_file = FileBrowseField("File", max_length=200, directory="media/")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')

    def __str__(self):
        return f"{self.media_type} for post {self.event.title}"