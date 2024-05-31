from django.contrib import admin
from . models import Club,ClubMembership,Post, Comment,Notification
# Register your models here.
admin.site.register(Club)
admin.site.register(ClubMembership)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)