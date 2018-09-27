# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=30)),
                ('projectDescribe', models.TextField()),
                ('is_active', models.BooleanField(default=True, help_text=b'Designates whether this project should be treated as active. ')),
            ],
        ),
    ]
