# Generated by Django 4.2.10 on 2024-02-28 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0002_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
