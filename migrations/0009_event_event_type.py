# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_eventtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(default=1, to='events.EventType'),
        ),
    ]
