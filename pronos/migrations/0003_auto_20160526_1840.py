# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0002_auto_20160526_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='stage',
            field=models.CharField(choices=[('A', 'Groupe A'), ('B', 'Groupe B'), ('C', 'Groupe C'), ('D', 'Groupe D'), ('E', 'Groupe E'), ('F', 'Groupe F'), ('QF', 'Quart de finale'), ('SF', 'Demi finale'), ('FI', 'Finale')], max_length=1),
        ),
    ]