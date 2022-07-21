# Requisito 6
from tech_news.database import search_news
from datetime import datetime


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
    try:
        if not bool(datetime.strptime(date, "%Y-%m-%d")):
            raise ValueError

        formatted_date = "/".join(reversed(date.split('-')))

        date_search = search_news(query={
            "timestamp":  formatted_date
            })

        news = [(news["title"], news["url"]) for news in date_search]

        return news

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    raw_data_list = search_news(query={
        "tags": {
            "$elemMatch": {
                "$regex": f"{tag}", "$options": "i"}
            }}
    )

    formatted_data = []

    for data in raw_data_list:
        formatted_data.append((
            data["title"], data["url"]),
        )

    return formatted_data


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
