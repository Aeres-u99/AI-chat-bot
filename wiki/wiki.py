import bs4 as bs
import urllib.request
import re

def retrieve(query):
    search_query = query
    search_query = search_query.replace(" ","_")
    print("Searching ... \n",search_query)

    base_url = "http://en.wikipedia.com/wiki/?search="
    search_url = base_url+search_query

    scaraped_data = urllib.request.urlopen(search_url)
    article = scaraped_data.read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
    article_text=""
    for p in paragraphs:
        article_text+=p.text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    return article_text

