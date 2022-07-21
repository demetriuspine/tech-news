# Requisito 6
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news(query={
            'title': {'$regex': title, "$options": "i"}
        })
    news_tuples_list = []

    for news in news_list:
        news_tuple = tuple([news['title'], news['url']])
        news_tuples_list.append(news_tuple)

    return news_tuples_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
