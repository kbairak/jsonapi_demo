from django.core.urlresolvers import reverse

from rest_framework import views
from rest_framework.response import Response

from articles.models import Article

from .serializers import (ArticleListResponseSerializer,
                          ArticleResponseSerializer)


class ArticleListView(views.APIView):
    def get(self, request):
        articles = Article.objects.select_related('author').all()
        data = ArticleListResponseSerializer(articles).data
        return Response(data)

    def post(self, request):
        serializer = ArticleResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = Article.objects.create(
            title=serializer.validated_data['title'],
            body=serializer.validated_data['body'],
            author=serializer.validated_data['author_id'],
        )
        return Response(
            ArticleResponseSerializer(article).data,
            status=201,
            headers={'Location': reverse("article",
                                         kwargs={'article_id': article.id})}
        )


class ArticleView(views.APIView):
    def get(self, request, article_id):
        article = Article.objects.select_related('author').get(id=article_id)
        data = ArticleResponseSerializer(article).data
        return Response(data)
