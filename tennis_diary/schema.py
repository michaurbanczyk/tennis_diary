import graphene

from players.schema.schema import players_schema


class Query(players_schema.PlayersQuery):
    hello = graphene.String(default_value="Hi!")


class Mutation(players_schema.PlayersMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
