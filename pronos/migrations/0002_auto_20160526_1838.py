# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='stage',
            field=models.CharField(choices=[('A', 'Groupe A'), ('B', 'Groupe B'), ('C', 'Groupe C'), ('D', 'Groupe D'), ('E', 'Groupe E'), ('F', 'Groupe F')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Stage',
        ),
    ]