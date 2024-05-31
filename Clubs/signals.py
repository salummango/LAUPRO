from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Notification

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        club_members = instance.post.club.clubmembership_set.values_list('user', flat=True)
        for member_id in club_members:
            notification = Notification.objects.create(
                user_id=member_id,
                message=f'New comment on post {instance.post.id}',
                link = f'/alumn_club/club/{instance.post.club.id}/post/{instance.post.id}'
            )


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Notification

@receiver(post_save, sender=Post)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        club_members = instance.club.clubmembership_set.values_list('user', flat=True)
        for member_id in club_members:
            notification = Notification.objects.create(
                user_id=member_id,
                message=f'New post in {instance.club.name}',
                link=f'/alumn_club/club/{instance.club.id}/post/{instance.id}'
            )
