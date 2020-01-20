from django.core.management.base import BaseCommand
from scraper.models import Article
from django.utils import timezone
import requests
import urllib3
from bs4 import BeautifulSoup


def remodel_content(raw_content):
    article_content = ''
    for tag in raw_content.children:
        # This long 'if' will filter out all tags that are not 'p' or 'h2', those who are embedded videos (that did not work for some reason), or the last paragraph (which is a text unrelated to the article)
        if (tag.name == "p" and (not tag.has_attr('class') or tag['class'][0] != 'video-center') and (tag.span == None or tag.span.get_text() != 'Cupons de desconto TecMundo:')) or tag.name == "h2":
            article_content = article_content + str(tag)
        # This 'if' will filter images and captions, and make it so they work properly on the portal
        elif tag.has_attr('class') and tag['class'][0] == 'video-center':
            article_content = article_content + '<iframe width="600" height="400" src="' + tag.span.iframe['data-src'].split('https:')[1] + '"></iframe>'
        elif tag.name == "figure":
            article_content = article_content + '<img style="max-width: 100%" src="' + \
                tag.img['data-src'].split('?')[0] + \
                '"><p class="caption">' + tag.figcaption.get_text() + '</p>'
    return article_content


def scrape():
    # URL Request and HTML parsing
    url = 'https://www.tecmundo.com.br/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Retrieves the list of articles on the 'highlight' carousel
    article_list = soup.find_all(class_='tec--carousel__item__title__link')

    # For each article, get the ID, URL, title and content
    for article in article_list:
        article_title = article.string
        article_url = article.get('href')
        article_id = article_url.split('/')[4].split('-')[0]
        response = requests.get(article_url)
        soup = BeautifulSoup(response.text, "html.parser")
        article_content_bs4 = soup.find(class_="tec--article__body")
        article_content = ""

        # Due to unlinked classes and other stuff, it's needed to rebuild the article itself, filtering out some stuff and remodeling others
        article_content = remodel_content(article_content_bs4)

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
