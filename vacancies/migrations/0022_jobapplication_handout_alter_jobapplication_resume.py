# Generated by Django 4.0.4 on 2022-05-27 05:43

from django.db import migrations, models
import vacancies.formatChecker


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0021_alter_jobapplication_github_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='handout',
            field=vacancies.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(help_text='Загрузить резюме*', upload_to='resumes/', verbose_name='Загрузить резюме*'),
        ),
    ]
