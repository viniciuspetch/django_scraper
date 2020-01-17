from django.shortcuts import render
from scraper.models import Article

def index(request):
    return render(request, 'scraper/index.html', {'article_list': Article.objects.all()})
