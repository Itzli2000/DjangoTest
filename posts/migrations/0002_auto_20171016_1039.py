# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.TextField(),
        ),
    ]