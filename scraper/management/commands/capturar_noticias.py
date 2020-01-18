from django.core.management.base import BaseCommand
from scraper.models import Article
from django.utils import timezone
import requests
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.tecmundo.com.br/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title_list = soup.find_all(class_='tec--carousel__item__title__link')
    for title in title_list:
        title_href = title.get('href')
        item_id = title_href.split('/')[4].split('-')[0]

        if len(Article.objects.filter(article_id=item_id)) == 0:
            Article(article_id=item_id, url=title_href,
                    title=title.string).save()
            print('!!NEW!! ('+item_id+') '+title.string)

        else:
            print('('+item_id+') '+title.string)


class Command(BaseCommand):
    help = 'Get the main article titles and URL'

    def handle(self, *args, **kwargs):
        scrape()
