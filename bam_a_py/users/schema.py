from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from bam_a_py.users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['name',]
        interfaces = (relay.Node, )


class Query(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
