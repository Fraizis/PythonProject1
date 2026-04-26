import os
from decimal import Decimal
from unicodedata import decimal

import requests
from bs4 import BeautifulSoup
import pandas as pd


# import sqlalchemy as sa
# from loguru import logger

# login = os.environ['login']
# password = os.environ['password']
# host = os.environ['host']


def load_to_db(df):
    connection_string = f"postgresql+psycopg2://{login}:{password}@{host}/postgres"
    engine = sa.create_engine(connection_string)

    with engine.connect() as connection:
        df.to_sql(name='techcrunch_articles', schema='public', con=connection, index=False, if_exists='append')
        connection.close()
    logger.info('загрузка завершена')


def parse_techcrunch(url):
    response = requests.get(url)
    logger.info(f'reesonse: {response}')
    articles_list = []
    soup = BeautifulSoup(response.content, 'html.parser')

    all_articles = soup.find_all('li', class_='wp-block-post')

    # Extract the required information from each article
    for article in all_articles:
        title_tag = article.find('a', class_='loop-card__title-link')
        title = title_tag.get_text(strip=True) if title_tag else 'no title'
        article_link = title_tag['href'] if title_tag else 'no link'

        category_tag = article.find('a', class_='loop-card__cat')
        category = category_tag.get_text(strip=True) if category_tag else 'no category'

        author_tag = article.find('a', class_='loop-card__author')
        author = author_tag.get_text(strip=True) if author_tag else 'no authors'

        image_tag = article.find('img')
        image_url = image_tag['src'] if image_tag else 'no image'

        date_tag = article.find('time')
        date_data = date_tag['datetime'] if date_tag else 'no date'

        response_article = requests.get(article_link)

        soup_article = BeautifulSoup(response_article.content, 'html.parser')
        article_tag = soup_article.find('p', id='speakable-summary')
        summary = article_tag.get_text(strip=True) if article_tag else 'no summary'

        articles_list.append({
            'title': title,
            'category': category,
            'author': author,
            'image_url': image_url,
            'date_data': date_data,
            'article_link': article_link,
            'summary': summary
        })

        df = pd.DataFrame(articles_list)

    return df


def main(event, context):
    url = "https://techcrunch.com/tag/apple/"
    df_example = parse_techcrunch(url)
    load_to_db(df_example)
    logger.info('парсер отработал успешно')


class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = 0.0
        self.set_balance(initial_balance)

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            print("Ошибка: баланс должен быть числом.")
            return

        if new_balance < 0:
            print("Ошибка: баланс не может быть отрицательным.")
            return

        self._balance = float(new_balance)
        print(f"Баланс успешно установлен: {self._balance}")


class Device:
    company = "FutureTech"

    def __init__(self, model_name, power):
        self.model_name = model_name
        self._power_level = power
        self.__secret_code = "XYZ123"

class Tech(Device):
    ...


dev = Device('tech', 100)
dev._Device__secret_code = '12345678'
t = Tech('tech', 100)
t._Device__secret_code = '12345678'
print(Device.__secret_code)
