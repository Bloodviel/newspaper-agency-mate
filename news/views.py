from django.shortcuts import render

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
