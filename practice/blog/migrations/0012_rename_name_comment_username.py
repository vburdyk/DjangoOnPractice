# Generated by Django 4.2 on 2023-04-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='username',
        ),
    ]
