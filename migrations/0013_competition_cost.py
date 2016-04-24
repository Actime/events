# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_orginizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
