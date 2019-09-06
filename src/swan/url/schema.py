# shortener/urls/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from swan.url.models import URL


class URLType(DjangoObjectType):
    hash_id = graphene.String(source='hash')

    class Meta:
        model = URL


class Query(object):
    url = graphene.Field(URLType,
                         id=graphene.Int(),
                         url=graphene.String(),
                         hash_id=graphene.String(),)

    all_urls = graphene.List(URLType)

    def resolve_all_urls(self, info, **kwargs):
        return URL.objects.all()

    def resolve_url(self, info, **kwargs):
        id = kwargs.get('id')
        url = kwargs.get('url')

        if id is not None:
            return URL.objects.get(pk=id)

        if url is not None:
            return URL.objects.get(url=url)

        return None


class CreateURL(graphene.Mutation):
    class Arguments:
        url = graphene.String()

    ok = graphene.Boolean()
    url = graphene.Field(lambda: URLType)

    @staticmethod
    def mutate(root, info, url=None):
        ok = True
        try:
            instance = URL.objects.get(url=url)
        except:
            instance = URL(url=url)
            instance.save()
        return CreateURL(ok=ok, url=instance)


class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()


