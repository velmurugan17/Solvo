import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.prnewswire.com"


def get_page_content(url):
    page = requests.get(url)
    return page.content


def soup_object_from_html_content(html_content):
    return BeautifulSoup(html_content, "html.parser")


def get_news_feed_page(page_number=1, number_of_feeds=25):
    news_feed_url = (
        f"{BASE_URL}/news-releases/news-releases-list/?page="
        f"{page_number}&pagesize={number_of_feeds}"
    )
    return get_page_content(news_feed_url)


def news_feed_filter(page_object):
    return page_object.find_all(attrs={"class": "row arabiclistingcards"})


def get_news_title(feed):
    try:
        return feed.find(name="img").get("title")
    except AttributeError:
        return ""


def get_news_time(feed):
    return feed.find(attrs={"name": "date"}).get("content")


def get_news_publisher(feed):
    return feed.find(attrs={"name": "author"}).get("content")


def get_news_feed_url(feed):
    return feed.find(
        attrs={"class": "newsreleaseconsolidatelink display-outline"}
    ).get("href")


def get_publisher_news_time_from_feed_url(feed_url):
    news_feed_url = f"{BASE_URL}{feed_url}"

    page_content = get_page_content(news_feed_url)
    soup_object = soup_object_from_html_content(page_content)

    author_name = get_news_publisher(soup_object)
    published_date = get_news_time(soup_object)

    return author_name, published_date


def parse_html_news_feed_to_elements(page_content):
    soup_object = soup_object_from_html_content(page_content)
    filtered_news_feed = news_feed_filter(soup_object)
    news_feed_data = []
    for feed in filtered_news_feed:
        news_title = get_news_title(feed)
        news_feed_url = get_news_feed_url(feed)
        author, published_date = get_publisher_news_time_from_feed_url(
            news_feed_url
        )
        news_feed_data.append(
            {
                "title": news_title,
                "url": f"{BASE_URL}{news_feed_url}",
                "author": author,
                "date": published_date,
            }
        )

    return news_feed_data


def main():
    html_page_content = get_news_feed_page(number_of_feeds=100)
    filtered_feeds = parse_html_news_feed_to_elements(html_page_content)
    with open("news_feed.json", "w") as nf:
        json.dump(filtered_feeds, nf)
        
    # :TODO:
    # 1. Define th logic to look for number of pages or last feed timestamp
    # 2. Scheduler to run every one hr to collect the latest data from last collected info
    # 3. Timezone conversion. Currently the timezone is in ET (Eastern Time)
    # 4. ...


if __name__ == "__main__":
    main()
