import factory

from worldcupprono.factories import UserFactory

from .models import Board


class BoardFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Board

    owner = factory.SubFactory(UserFactory)
    name = factory.Faker('words', nb=3)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Override to play the perform_create behavior like API
        """
        board = super(BoardFactory, cls)._create(model_class, *args, **kwargs)
        board.users.add(board.owner)

        return board
