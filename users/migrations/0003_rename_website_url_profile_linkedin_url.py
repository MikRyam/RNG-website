# Generated by Django 4.0.4 on 2022-05-25 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='website_url',
            new_name='linkedin_url',
        ),
    ]
