# Generated by Django 3.2.1 on 2022-02-08 08:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('msg', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
