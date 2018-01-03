from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Pays", unique=True)
    code = models.CharField(
        max_length=3, verbose_name="Code pays", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @property
    def meta(self):
        return self._meta

    @property
    def contenttype(self):
        return ContentType.objects.get_for_model(self)

    @property
    def class_name(self):
        return self.__class__.__name__


class Match(models.Model):
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
    score_domicile = models.IntegerField(blank=True, default=0)
    score_visitor = models.IntegerField(blank=True, default=0)
    stage = models.CharField(max_length=2, choices=STAGE_CHOICES)
    date = models.DateTimeField(verbose_name="Date du match", db_index=True)
    pronos = models.ManyToManyField(User, through='Prono')

    def __str__(self):
        return "{} - {} vs {}".format(
            self.get_stage_display(), self.team_domicile, self.team_visitor)

    class Meta:
        ordering = ['date']

    @property
    def meta(self):
        return self._meta

    @property
    def contenttype(self):
        return ContentType.objects.get_for_model(self)

    @property
    def class_name(self):
        return self.__class__.__name__


class Prono(models.Model):
    # Type
    TYPE_WIN = 'V'
    TYPE_DRAW = 'N'
    TYPE_LOSE = 'D'

    TYPE_CHOICES = (
        (TYPE_WIN, "Victoire de l'équipe à domicile"),
        (TYPE_DRAW, "Match nul"),
        (TYPE_LOSE, "Défaite de l'équipe à domicile")
    )

    prono = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_DRAW)
    points = models.IntegerField(blank=True, default=0)
    score_domicile = models.IntegerField(default=0)
    score_visitor = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="pronos")
    match = models.ForeignKey(Match, related_name="users")
    modified = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True,
        db_index=True)

    def __str__(self):
        return u'Match: %s - User id: %s' % (self.match.pk, self.user.pk)

    class Meta:
        unique_together = ("match", "user")

    @property
    def meta(self):
        return self._meta

    @property
    def contenttype(self):
        return ContentType.objects.get_for_model(self)

    @property
    def class_name(self):
        return self.__class__.__name__
