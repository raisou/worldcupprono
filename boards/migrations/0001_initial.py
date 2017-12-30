# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 17:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date de création')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Participants')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
