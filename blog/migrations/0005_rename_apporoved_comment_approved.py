# Generated by Django 4.2.10 on 2024-02-13 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_content_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='apporoved',
            new_name='approved',
        ),
    ]
