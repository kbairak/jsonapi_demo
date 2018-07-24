from django.conf.urls import url
from rest_framework import routers
from .views import ArticleViewSet, UserViewSet, AuthorView


router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls + [url(
    regex=r'^articles/(?P<pk>[^/.]+)/relationships/(?P<related_field>[^/.]+)$',
    view=AuthorView.as_view(),
    name='article-user-relationships'
)]
