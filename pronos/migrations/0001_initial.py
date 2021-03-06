# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 14:03
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
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(blank=True, choices=[('V', "Victoire de l'équipe à domicile"), ('N', 'Match nul'), ('D', "Défaite de l'équipe à domicile")], editable=False, max_length=1)),
                ('score_domicile', models.PositiveSmallIntegerField(default=0)),
                ('score_visitor', models.PositiveSmallIntegerField(default=0)),
                ('stage', models.CharField(choices=[('A', 'Groupe A'), ('B', 'Groupe B'), ('C', 'Groupe C'), ('D', 'Groupe D'), ('E', 'Groupe E'), ('F', 'Groupe F'), ('G', 'Groupe G'), ('H', 'Groupe H'), ('HF', 'Huitième de finale'), ('QF', 'Quart de finale'), ('SF', 'Demi finale'), ('FI', 'Finale')], max_length=2)),
                ('date', models.DateTimeField(db_index=True, verbose_name='Date du match')),
                ('played', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Prono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(blank=True, choices=[('V', "Victoire de l'équipe à domicile"), ('N', 'Match nul'), ('D', "Défaite de l'équipe à domicile")], editable=False, max_length=1)),
                ('score_domicile', models.PositiveSmallIntegerField(default=0)),
                ('score_visitor', models.PositiveSmallIntegerField(default=0)),
                ('points', models.IntegerField(blank=True, default=0)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date de modification')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='pronos.Match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pronos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Pays')),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Code pays')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='match',
            name='pronos',
            field=models.ManyToManyField(through='pronos.Prono', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='team_domicile',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='as_domicile', to='pronos.Team', verbose_name='Equipe domicile'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_visitor',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='as_visitor', to='pronos.Team', verbose_name='Equipe exterieur'),
        ),
        migrations.AlterUniqueTogether(
            name='prono',
            unique_together=set([('match', 'user')]),
        ),
    ]
