import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    urls_list = selector.css(".cs-overlay-link::attr(href)").getall()

    return urls_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next.page-numbers::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    title = (selector.css("h1.entry-title::text").get()).strip()
    url = selector.css("[rel='canonical']::attr(href)").get()
    timestamp = selector.css("ul.post-meta > li.meta-date ::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = selector.css("div.comment-respond").getall()
    summary = selector.css(
        ".entry-content > p:nth-of-type(1) ::text"
    ).getall()
    summary = ''.join(summary)
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    scraped_news_dict = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments_count),
        "summary": summary.strip(),
        "tags": tags,
        "category": category
    }

    return scraped_news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    BASE_URL = "https://blog.betrybe.com"
    html_content = fetch(url=BASE_URL)
    urls_list = scrape_novidades(html_content=html_content)
    news_list = []

    while len(urls_list) < amount:
        next_page_link = scrape_next_page_link(html_content=html_content)
        html_content = fetch(url=next_page_link)
        urls_list.extend(scrape_novidades(html_content=html_content))

    for url in urls_list[:amount]:
        page_content = fetch(url=url)
        scrape_content = scrape_noticia(html_content=page_content)
        news_list.append(scrape_content)

    create_news(news_list)
    return news_list
