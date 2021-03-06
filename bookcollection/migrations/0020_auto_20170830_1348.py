# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-30 13:48
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0019_auto_20170825_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subgenre',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='genre', chained_model_field='genre', default=1, on_delete=django.db.models.deletion.CASCADE, to='bookcollection.Subgenre'),
            preserve_default=False,
        ),
    ]
