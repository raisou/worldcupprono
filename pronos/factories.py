import factory
from django.utils.timezone import get_current_timezone

from worldcupprono.factories import UserFactory

from .models import (Team, Match, Prono)


class TeamFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Team
        django_get_or_create = ('name', 'code')

    name = factory.Faker('country')
    code = factory.Faker('country_code')


class MatchFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Match

    team_domicile = factory.SubFactory(TeamFactory)
    team_visitor = factory.SubFactory(TeamFactory)
    stage = "A"
    date = factory.Faker(
        'future_datetime', end_date="+1y", tzinfo=get_current_timezone())


class PronoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Prono

    user = factory.SubFactory(UserFactory)
    match = factory.SubFactory(MatchFactory)
