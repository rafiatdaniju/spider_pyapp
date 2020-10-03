import requests
from decouple import config
from celery import Celery
from .db import DB
from bs4 import BeautifulSoup
import re
import time


def fetch_record(page_id):
    try:
        record=DB.pages().find(page_id)
        DB.pages().update(page_id,'true')
        url_address = record[1]
    
        content = requests.get(url_address)
        soup = BeautifulSoup(content.text, features='html.parser')
        list_of_links = []
        for link in soup.find_all('a', href = True):
            links = link['href']
            if re.search('^https', links):
                list_of_links.append(links)
        first_10 = list_of_links[:10]
        DB.links().delete(page_id)
        for link in first_10:
            DB.links().insert(page_id,link)
        record=DB.pages().update(page_id,'false')
    except Exception as err:
        print('id not found', err)
    
    
