# Generated by Django 3.2.1 on 2022-02-05 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='media/team/%Y/%m/%d/'),
        ),
    ]
