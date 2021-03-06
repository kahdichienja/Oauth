# Generated by Django 2.1.7 on 2019-03-05 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/blogphotos/')),
            ],
        ),
    ]
