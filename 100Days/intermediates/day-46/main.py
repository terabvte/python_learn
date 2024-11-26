import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lxml
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://example.com"


date_travel = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

r = requests.get(
    f"https://www.billboard.com/charts/hot-100/{date_travel}", headers=header
)
page = r.text

soup = BeautifulSoup(page, "lxml")

title_tags = soup.select(selector="li #title-of-a-story")
titles = []
i = 1
for title in title_tags:
    titles.append(f"{i}) {title.text.replace("\n", "").replace("\t", "")}")
    i = i + 1
[print(title) for title in titles]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
    )
)
lz_uri = "spotify:artist:36QJpDe2go2KgaRleHCDTp"
results = sp.artist_top_tracks(lz_uri)
# Test:
for track in results["tracks"][:10]:
    print("track    : " + track["name"])
    print("audio    : " + track["preview_url"])
    print("cover art: " + track["album"]["images"][0]["url"])
    print()
