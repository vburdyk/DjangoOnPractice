# Generated by Django 4.2 on 2023-04-26 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
