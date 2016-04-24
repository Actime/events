# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='orginizer',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
