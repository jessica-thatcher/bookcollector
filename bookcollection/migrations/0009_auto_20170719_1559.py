# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0008_book_audiobook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subgenre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookcollection.Subgenre'),
        ),
    ]