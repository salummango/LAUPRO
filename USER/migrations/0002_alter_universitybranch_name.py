# Generated by Django 5.0.6 on 2024-05-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitybranch',
            name='name',
            field=models.CharField(choices=[('Tunguu Campus', 'Tunguu'), ('Maruhubi Campus', 'Maruhubi'), ('Kilimani Campus', 'Kilimani'), ('Kizimbani Campus', 'Kizimbani'), ('Vuga Campus', 'Vuga'), ('Chwaka Campus', 'Chwaka')], max_length=100),
        ),
    ]
