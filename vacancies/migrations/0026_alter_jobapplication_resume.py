# Generated by Django 4.0.4 on 2022-05-27 07:29

from django.db import migrations
import vacancies.formatChecker


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0025_remove_jobapplication_handout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=vacancies.formatChecker.ContentTypeRestrictedFileField(help_text='Загрузить резюме в формате txt, doc, docx, pdf', upload_to='resumes/', verbose_name='Загрузить резюме*'),
        ),
    ]
