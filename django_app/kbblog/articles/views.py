from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework_json_api.views import RelationshipView

from .models import Article
from .serializers import ArticleSerializer, UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorView(RelationshipView):
    queryset = User.objects
