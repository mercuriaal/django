from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    articles = Article.objects.all().order_by('-published_at')
    context['object_list'] = articles

    return render(request, template, context)
