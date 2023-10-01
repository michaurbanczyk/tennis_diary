from graphene import relay
from graphene_django import DjangoObjectType

from players.models import Player


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player
        filter_fields = "__all__"
        interfaces = (relay.Node,)
