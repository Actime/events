# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_competition_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.TextField(default=b''),
        ),
    ]
