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
    title_list = soup.find_all(class_='tec--carousel__item__title__link')

    # For each article, get the 'title', 'URL' and 'ID' (based on the URL itself). In this initial version, we're only getting articles from Tecmundo, so the 'source' is hardcoded as such
    for title in title_list:
        title_href = title.get('href')
        item_id = title_href.split('/')[4].split('-')[0]

        # If the ID is not found, it's considered a new article, so it's added to the DB
        if len(Article.objects.filter(article_id=item_id)) == 0:
            Article(source='Tecmundo', article_id=item_id, url=title_href,
                    title=title.string).save()
            print('!!NEW!! ('+item_id+') '+title.string)
        # Otherwise, only show on the console
        else:
            print('('+item_id+') '+title.string)


class Command(BaseCommand):
    help = 'Get the main article titles and URL'

    def handle(self, *args, **kwargs):
        scrape()
