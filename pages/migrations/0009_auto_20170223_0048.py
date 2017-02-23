# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_page_leave_capture'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='jumbtron_bg_color',
            field=models.CharField(default='#eeeeee', max_length=7, validators=[pages.models.layout_validator]),
        ),
        migrations.AddField(
            model_name='page',
            name='jumbtron_text_color',
            field=models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validator]),
        ),
    ]