import graphene

import swan.url.schema


class Query(swan.url.schema.Query, graphene.ObjectType):
    pass


class Mutation(swan.url.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
