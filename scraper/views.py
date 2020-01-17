from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'scraper/index.html', context)
