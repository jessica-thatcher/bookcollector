# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0024_book_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='storage',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]