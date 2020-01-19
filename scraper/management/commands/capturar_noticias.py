from django.core.management.base import BaseCommand
from scraper.models import Article
from django.utils import timezone
import requests
from bs4 import BeautifulSoup


def scrape():
    # URL Request and HTML parsing
    url = 'https://www.tecmundo.com.br/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Retrieves the list of articles on the 'highlight' carousel
    article_list = soup.find_all(class_='tec--carousel__item__title__link')

    # For each article, get the ID, URL, title and content
    article = article_list[0]
    article_title = article.string
    article_url = article.get('href')
    article_id = article_url.split('/')[4].split('-')[0]
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, "html.parser")
    article_content_bs4 = soup.find(class_="tec--article__body")
    article_content = ""

    for tag in article_content_bs4.children:
        print(tag.name)
        if tag.name == "p" or tag.name == "h2":
            article_content = article_content + str(tag)
        if tag.name == "figure":
            img = tag.img
            print(img['data-src'].split('?')[0])
            print(type(img))
            article_content = article_content + '<img src="' + img['data-src'].split('?')[0] + '">' + str(tag.figcaption)


    # If the ID is not found, it's considered a new article, so it's added to the DB
    if len(Article.objects.filter(article_id=article_id)) == 0:
        Article(source='Tecmundo', article_id=article_id, url=article_url,
                title=article_title, content=article_content).save()
        print('!!NEW!! ('+article_id+') '+article_title)
    # Otherwise, only show on the console
    else:
        print('('+article_id+') '+article_title)


class Command(BaseCommand):
    help = 'Get the main article titles and URL'

    def handle(self, *args, **kwargs):
        scrape()
