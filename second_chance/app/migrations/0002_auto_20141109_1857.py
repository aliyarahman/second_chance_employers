# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industry',
            name='employers',
        ),
        migrations.RemoveField(
            model_name='industry',
            name='phone',
        ),
        migrations.AddField(
            model_name='employer',
            name='industries',
            field=models.ManyToManyField(to='app.Industry', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 768776), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 768794), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='industry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 768285), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='industry',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 768312), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 769885), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 769904), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userreview',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 770386), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userreview',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 57, 15, 770405), auto_now=True),
            preserve_default=True,
        ),
    ]
