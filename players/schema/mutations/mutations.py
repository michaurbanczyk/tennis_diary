import graphene
from graphene import Field, relay

from players.models import Player
from players.types.types import PlayerType


class AddPlayerInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    middle_name = graphene.String(required=False)
    last_name = graphene.String(required=True)
    birth_date = graphene.Date(required=False)
    nick_name = graphene.String(required=False)
    ntrp = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=False)
    age = graphene.String(required=False)
    height = graphene.String(required=False)
    weight = graphene.String(required=False)


class AddPlayerMutation(relay.ClientIDMutation):
    class Input:
        add_player = graphene.Argument(AddPlayerInput)

    player = Field(lambda: PlayerType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, add_player):
        """Create a new player."""
        player = Player.objects.create(**add_player)
        return AddPlayerMutation(player=player)


class PlayersMutation(graphene.ObjectType):
    add_player = AddPlayerMutation.Field()
