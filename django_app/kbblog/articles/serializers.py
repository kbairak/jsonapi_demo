from django.contrib.auth.models import User

from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'created', 'modified', 'author')

    author = ResourceRelatedField(
        queryset=User.objects,
        related_link_view_name='user-detail',
        related_link_url_kwarg='pk',
        self_link_view_name='article-user-relationships'
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
