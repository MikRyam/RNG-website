# Generated by Django 4.0.4 on 2022-05-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0009_vacancy_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='onTop',
            field=models.BooleanField(default=False, verbose_name='Разместить вакансию в топе'),
        ),
    ]
