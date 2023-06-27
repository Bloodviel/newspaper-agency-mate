from django.urls import path

from news.views import index, TopicsListView, NewspaperListView, RedactorListView

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicsListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
]

app_name = "news"
