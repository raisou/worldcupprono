from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .mixins import BasePronoModelMixin


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Pays", unique=True)
    code = models.CharField(
        max_length=3, verbose_name="Code pays", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Match(BasePronoModelMixin):
    STAGE_CHOICES = (
        ("A", "Groupe A"),
        ("B", "Groupe B"),
        ("C", "Groupe C"),
        ("D", "Groupe D"),
        ("E", "Groupe E"),
        ("F", "Groupe F"),
        ("G", "Groupe G"),
        ("H", "Groupe H"),
        ("HF", "Huitième de finale"),
        ("QF", "Quart de finale"),
        ("SF", "Demi finale"),
        ("FI", "Finale")
    )

    team_domicile = models.ForeignKey(
        Team,
        max_length=150,
        verbose_name="Equipe domicile",
        related_name="as_domicile")
    team_visitor = models.ForeignKey(
        Team,
        max_length=150,
        verbose_name="Equipe exterieur",
        related_name="as_visitor")
    stage = models.CharField(max_length=2, choices=STAGE_CHOICES)
    date = models.DateTimeField(verbose_name="Date du match", db_index=True)
    pronos = models.ManyToManyField(User, through='Prono')
    played = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} vs {}".format(
            self.get_stage_display(), self.team_domicile, self.team_visitor)

    class Meta:
        ordering = ['date']

    @property
    def is_locked(self):
        day_before = self.date - timedelta(days=1)
        return timezone.now() > day_before


class Prono(BasePronoModelMixin):
    points = models.IntegerField(blank=True, default=0)
    user = models.ForeignKey(User, related_name="pronos")
    match = models.ForeignKey(Match, related_name="users")
    modified = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True,
        db_index=True)

    def __str__(self):
        return 'Match: {} - User: {}'.format(self.match.pk, self.user.pk)

    class Meta:
        unique_together = ("match", "user")
