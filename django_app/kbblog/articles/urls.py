from django.conf.urls import url

from .views import ArticleView, ArticlesView

urlpatterns = [
    url(regex=r'^articles$',
        view=ArticlesView.as_view(),
        name="articles"),
    # Firefox automatically appends a '/'
    url(regex=r'^articles/$',
        view=ArticlesView.as_view(),
        name="articles"),
    url(regex=r'^articles/(?P<article_id>\d+)$',
        view=ArticleView.as_view(),
        name="article"),
]
