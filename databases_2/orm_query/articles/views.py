from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    articles = Article.objects.only('title', 'text').order_by('-published_at')
    genres = Article.objects.select_related('genre').order_by('-published_at')
    authors = Article.objects.select_related('author').order_by('-published_at')
    context = {'articles': articles, 'articles_genres': genres, 'articles_authors': authors}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template_name, context)
