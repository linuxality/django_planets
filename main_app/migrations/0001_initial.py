# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('distance', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
