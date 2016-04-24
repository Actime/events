# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ubication',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
