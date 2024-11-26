from bs4 import BeautifulSoup
import lxml
import requests

r = requests.get("https://news.ycombinator.com/news")
peji = r.text

soup = BeautifulSoup(peji, "lxml")
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    if article_tag.select_one(selector="span"):
        continue
    text = article_tag.text
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.text.split()[0] )for score in soup.select(selector=".score")]

print(article_texts)
print(article_links)
print(article_upvotes)

print("\n")

# How 2 get the maxx it fors

top_article = article_upvotes.index(max(article_upvotes))
print(article_texts[top_article])
print(article_links[top_article])
print(article_upvotes[top_article])
