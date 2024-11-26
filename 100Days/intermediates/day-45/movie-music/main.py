import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

r = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
page = r.text

soup = BeautifulSoup(page, "lxml")
# print(soup.prettify())

movie_tags = soup.select(selector="section div .title")
movie_titles = []
for movie in movie_tags:
    text = movie.text
    movie_titles.append(text)
movie_titles.reverse()

with open("./100Days/intermediates/day-45/movie-music/movies.txt", mode="w+") as file:
    [file.write(f"{title}\n") for title in movie_titles]

# [print(title) for title in movie_titles]
