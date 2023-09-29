import graphene

from players.models import Player
from players.types.types import PlayerType


class PlayersQuery(graphene.ObjectType):
    all_players = graphene.List(PlayerType)

    def resolve_all_players(root, info):
        return Player.objects.all()
