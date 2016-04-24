# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('description', models.TextField(default=b'')),
                ('age_1', models.IntegerField(default=0)),
                ('age_2', models.IntegerField(default=0)),
                ('color', models.CharField(default=b'', unique=True, max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('description', models.TextField(default=b'')),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_finish', models.DateTimeField(blank=True)),
                ('image_url', models.TextField(default=b'')),
                ('competitors_limit', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='events.Category', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('description', models.TextField(default=b'')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('description', models.TextField(default=b'')),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_finish', models.DateTimeField(blank=True)),
                ('image_url', models.TextField(default=b'')),
                ('date_limit', models.DateTimeField(blank=True)),
                ('competitors_limit', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='competition_type',
            field=models.ForeignKey(default=1, to='events.CompetitionType'),
        ),
        migrations.AddField(
            model_name='competition',
            name='event',
            field=models.ForeignKey(default=1, to='events.Event'),
        ),
        migrations.AddField(
            model_name='competition',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
