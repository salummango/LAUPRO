from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from filebrowser.fields import FileBrowseField
from django.conf import settings
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alumn_posts')
    body = models.TextField()  # You may want to use a TextField for rich text content
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

    objects=models.Manager()
    published=PublishedManager()

    def get_absolute_url(self):
        return reverse("alumni:post_detail", args=[self.publish.year,self.publish.month,self.publish.day,self.slug])


class Media(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media_file = FileBrowseField("File", max_length=200, directory="media/")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')

    def __str__(self):
        return f"{self.media_type} for post {self.post.title}"