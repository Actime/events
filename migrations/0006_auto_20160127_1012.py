# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_competition_competition_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image_url',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
