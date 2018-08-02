from rest_framework import views
from rest_framework.response import Response

from articles.models import Article

from .serializers import (ArticleListResponseSerializer,
                          ArticleResponseSerializer)


class ArticlesView(views.APIView):
    def get(self, request):
        articles = Article.objects.select_related('author').all()
        data = ArticleListResponseSerializer(articles).data
        return Response(data)

    def post(self, request):
        serializer = ArticleResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # .validated_data looks like: {"type": "articles",
        #                              "title": "hello world",
        #                              "body": "hello world",
        #                              "author": {"id": "2",
        #                                         "type": "users"}}
        article = Article.objects.create(
            title=serializer.validated_data['title'],
            body=serializer.validated_data['body'],
            author_id=serializer.validated_data['author']['id'],
        )
        return Response(ArticleResponseSerializer(article).data)


class ArticleView(views.APIView):
    def get(self, request, article_id):
        article = Article.objects.select_related('author').get(id=article_id)
        data = ArticleResponseSerializer(article).data
        return Response(data)
