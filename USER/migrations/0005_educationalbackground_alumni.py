# Generated by Django 5.0.6 on 2024-05-31 14:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0004_otherinfo_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalbackground',
            name='alumni',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='educational_background', to=settings.AUTH_USER_MODEL),
        ),
    ]