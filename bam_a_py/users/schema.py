from graphene import relay, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from bam_a_py.users.serializers import UserSerializer

from bam_a_py.users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ('username', 'name', 'email', 'id')
        filter_fields = ['name',]
        interfaces = (relay.Node, )

    @classmethod
    def get_node(cls, info, id):
        if not info.context.user.is_authenticated():
            return None
        else:
            return User.objects.get(pk=id)


class Query(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    def resolve_all_users(self, info):
        if not info.context.user.is_authenticated():
            return User.objects.none()
        else:
            return User.objects.all().filter()
