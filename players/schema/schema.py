import graphene

from players.schema.mutations.mutations import PlayersMutation
from players.schema.queries.queries import PlayersQuery

players_schema = graphene.Schema(query=PlayersQuery, mutation=PlayersMutation)
