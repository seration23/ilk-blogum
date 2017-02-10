# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('olmuyor', '0002_auto_20170211_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='yaratilma_tarihi',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
