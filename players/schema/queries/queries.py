import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from players.types.types import PlayerType


class PlayersQuery(graphene.ObjectType):
    player = relay.Node.Field(PlayerType)
    all_players = DjangoFilterConnectionField(PlayerType)
