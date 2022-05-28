# Generated by Django 4.0.4 on 2022-05-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0017_alter_jobapplication_cover_letter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(verbose_name='Cover letter'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(upload_to='resumes/'),
        ),
    ]
