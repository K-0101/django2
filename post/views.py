from django.shortcuts import render
from .models import Article


def index(request):
    query = request.GET.get('q')

    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)