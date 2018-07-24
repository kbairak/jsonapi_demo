from django.db import models


class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('auth.User')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class JSONAPIMeta:
        resource_name = "articles"
