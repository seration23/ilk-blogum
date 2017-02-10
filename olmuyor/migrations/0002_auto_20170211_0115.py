# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('olmuyor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='yaratilma_tarihi',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 10, 22, 15, 55, 320669, tzinfo=utc)),
        ),
    ]
