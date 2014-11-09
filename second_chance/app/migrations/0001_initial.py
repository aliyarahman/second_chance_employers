# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40, null=True, blank=True)),
                ('email', models.EmailField(max_length=255, null=True, blank=True)),
                ('hq_address', models.CharField(max_length=255, null=True, blank=True)),
                ('hq_in_dc', models.BooleanField(default=False)),
                ('home_url', models.CharField(max_length=255, null=True, blank=True)),
                ('employment_url', models.CharField(max_length=255, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('box_present', models.IntegerField(null=True, blank=True)),
                ('crime_type_asked', models.IntegerField(null=True, blank=True)),
                ('years_specified_by_box', models.IntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 241394), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 241419), auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40, null=True, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 241880), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 241899), auto_now=True)),
                ('employers', models.ManyToManyField(to='app.Employer', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40, null=True, blank=True)),
                ('worksite_location', models.CharField(max_length=255, null=True, blank=True)),
                ('job_posted', models.CharField(max_length=40, null=True, blank=True)),
                ('collateral_sanction_applies', models.BooleanField(default=True)),
                ('which_collateral_sanction_applies', models.CharField(max_length=200, null=True, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 242915), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 242934), auto_now=True)),
                ('employer', models.ForeignKey(to='app.Employer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('notes', models.TextField(null=True, blank=True)),
                ('date_of_action', models.CharField(max_length=40, null=True, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 243407), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 11, 13, 243427), auto_now=True)),
                ('employer', models.ForeignKey(to='app.Employer')),
                ('position', models.ForeignKey(blank=True, to='app.Position', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
