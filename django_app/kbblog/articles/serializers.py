from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.Serializer):
    """ Usage:

        >>> ArticleSerializer(article).data
            {
                "id": "1",
                "type": "articles",
                "attributes": {
                    "title": "jsonapi is great",
                    "body": "jsonapi is great",
                    "created": "2018-08-01T13:08:28.843591Z",
                    "modified": "2018-08-01T13:08:28.843800Z"
                },
                "relationships": {
                    "author": {
                        "links": {"self": "/articles/1/relationships/author",
                                  "related": "/users/2"},
                        "data": {"type": "users", "id": 2}
                    }
                },
                "links": {"self": "/articles/1"}
            }
    """

    id = serializers.CharField(read_only=True)

    type = serializers.CharField(source="_meta.verbose_name_plural")

    def validate_type(self, value):
        if value != "articles":
            raise serializers.ValidationError("type '{}' should be 'articles'".
                                              format(value))
        return value

    class Attributes(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', 'body', 'created', 'modified')

    attributes = Attributes(source="*")

    class RelationShips(serializers.Serializer):
        class Author(serializers.Serializer):
            class Links(serializers.Serializer):
                self = serializers.SerializerMethodField()

                def get_self(self, obj):
                    return "/articles/{}/relationships/author".format(obj.id)

                related = serializers.SerializerMethodField()

                def get_related(self, obj):
                    return "/users/{}".format(obj.author_id)

            links = Links(source="*", required=False)

            class Data(serializers.Serializer):
                id = serializers.PrimaryKeyRelatedField(
                    source="author_id", queryset=User.objects.all()
                )

                type = serializers.CharField(
                    source="author._meta.verbose_name_plural"
                )

                def validate_type(self, value):
                    if value != "users":
                        raise serializers.ValidationError(
                            "type '{}' should be 'users'".format(value)
                        )
                    return value

            data = Data(source="*")

        author = Author(source="*")

    relationships = RelationShips(source="*")

    class Links(serializers.Serializer):
        self = serializers.SerializerMethodField()

        def get_self(self, obj):
            return "/articles/{}".format(obj.id)

    links = Links(source="*", required=False)


class ArticleResponseSerializer(serializers.Serializer):
    """ Usage:

        To read:
        >>> ArticleResponseSerializer(article).data
            {"links": {"self": "/articles/1"}, "data": {...}}

        To create:
        >>> serializer = ArticleResponseSerializer(data=request.data)
        >>> serializer.is_valid(raise_exception=True)
        >>> Article.objects.create(
        ...     title=serializer.validated_data['title'],
        ...     body=serializer.validated_data['body'],
        ...     author_id=serializer.validated_data['author']['id'],
        ... )
    """

    class Links(serializers.Serializer):
        self = serializers.SerializerMethodField()

        def get_self(self, obj):
            return reverse("article", kwargs={'article_id': obj.id})

    links = Links(source="*", required=False)

    data = ArticleSerializer(source="*")


class ArticleListResponseSerializer(serializers.Serializer):
    """ Usage:

        >>> ArticleListResponseSerializer(articles).data
            {"links": {"self": "/articles",
                       "next": "/articles?page[cursor]=XXX",
                       "prev": "/articles?page[cursor]=XXX",
                       "first": "/articles?page[cursor]=XXX",
                       "last": "/articles?page[cursor]=XXX"},
             "data": [...]}
    """

    class Links(serializers.Serializer):
        self = serializers.SerializerMethodField()

        def get_self(self, obj):
            return "/articles"

        next = serializers.SerializerMethodField()

        def get_next(next, obj):
            return "/articles"

        prev = serializers.SerializerMethodField()

        def get_prev(self, obj):
            return "/articles"

        first = serializers.SerializerMethodField()

        def get_first(self, obj):
            return "/articles"

        last = serializers.SerializerMethodField()

        def get_last(self, obj):
            return "/articles"

    links = Links(source="*")

    data = ArticleSerializer(source="*", many=True)
