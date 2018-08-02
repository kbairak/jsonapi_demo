from django.conf.urls import url

from .views import ArticleView, ArticleListView

urlpatterns = [
    url(regex=r'^articles$',
        view=ArticleListView.as_view(),
        name="article_list"),
    # Firefox automatically appends a '/'
    url(regex=r'^articles/$',
        view=ArticleListView.as_view(),
        name="article_list"),
    url(regex=r'^articles/(?P<article_id>\d+)$',
        view=ArticleView.as_view(),
        name="article"),
]
