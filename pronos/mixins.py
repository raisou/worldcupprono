from django.db import models


class BasePronoModelMixin(models.Model):
    # Type
    TYPE_WIN = 'V'
    TYPE_DRAW = 'N'
    TYPE_LOSE = 'D'

    TYPE_CHOICES = (
        (TYPE_WIN, "Victoire de l'équipe à domicile"),
        (TYPE_DRAW, "Match nul"),
        (TYPE_LOSE, "Défaite de l'équipe à domicile")
    )

    result = models.CharField(
        max_length=1, choices=TYPE_CHOICES, blank=True, editable=False)
    score_domicile = models.PositiveSmallIntegerField(default=0)
    score_visitor = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.score_domicile == self.score_visitor:
            self.result = self.TYPE_DRAW
        elif self.score_domicile > self.score_visitor:
            self.result = self.TYPE_WIN
        else:
            self.result = self.TYPE_LOSE

        super(BasePronoModelMixin, self).save(*args, **kwargs)
