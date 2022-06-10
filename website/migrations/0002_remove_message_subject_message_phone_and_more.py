# Generated by Django 4.0.4 on 2022-06-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(default=89991234567, max_length=30, verbose_name=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, max_length=2800, null=True, verbose_name=''),
        ),
    ]
