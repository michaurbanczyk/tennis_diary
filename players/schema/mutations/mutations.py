import graphene
from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation

from players.forms.forms import PlayerForm
from players.types.types import PlayerType


class AddPlayerMutation(DjangoModelFormMutation):
    player = Field(PlayerType)

    class Meta:
        form_class = PlayerForm


class UpdatePlayerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    data = Field(PlayerType)
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate(cls, form, info, id):
        print(id)
        return UpdatePlayerMutation(data=None, errors=["User does not exist"])


class PlayersMutation(graphene.ObjectType):
    add_player = AddPlayerMutation.Field()
    update_player = UpdatePlayerMutation.Field()
