from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.tecmundo.com.br/'
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    title_list = soup.find_all(class_='tec--carousel__item__title__link')
    for title in title_list:
        title_href = title.get('href')
        item_id = title_href.split('/')[4].split('-')[0]
        print('('+item_id+') '+title.string)
        print(title_href)


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        scrape()
