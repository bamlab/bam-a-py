import graphene
import bam_a_py.users.schema
import bam_a_py.taskapp.celery
import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

class Query(bam_a_py.users.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Add(graphene.Mutation):
    class Arguments:
        a = graphene.Float()
        b = graphene.Float()

    result = graphene.Float()

    def mutate(self, info, a, b):
        task = bam_a_py.taskapp.celery.add.delay(a, b)

        return Add(result=task.get())


class Mutation(graphene.ObjectType):
    add = Add.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
