# Generated by Django 4.2 on 2023-04-20 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_author_post_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]