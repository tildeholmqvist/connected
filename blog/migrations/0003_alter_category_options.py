# Generated by Django 4.2.10 on 2024-02-13 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
