from django.db import models
from swan.codec.base62 import base62


class URLQuerySet(models.QuerySet):
    def get(self, *args, **kwargs):
        hash_id = kwargs.get('hash_id')
        if hash_id:
            id = base62.decode(hash_id)
            return super().get(id=id)
        else:
            return super().get(*args, **kwargs)


class URLManager(models.Manager.from_queryset(URLQuerySet)):
    pass


class URL(models.Model):
    url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = URLManager()
    
    @property
    def hash(self) -> str:
        return base62.encode(self.id)
    

    def __str__(self):
        return self.url
