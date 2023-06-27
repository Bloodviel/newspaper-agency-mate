from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from news.models import Redactor, Newspaper, Topic


def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper. objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topic": num_topics
    }

    return render(request, "news/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic


class TopicDetailView(generic.DetailView):
    model = Topic


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.select_related("topic")


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class RedactorListView(generic.ListView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers")


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers__topic")
