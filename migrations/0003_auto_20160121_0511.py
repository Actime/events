# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160108_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
