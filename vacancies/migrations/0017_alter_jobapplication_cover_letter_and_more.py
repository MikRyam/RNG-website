# Generated by Django 4.0.4 on 2022-05-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0016_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(blank=True, null=True, verbose_name='Cover letter'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='salary',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
