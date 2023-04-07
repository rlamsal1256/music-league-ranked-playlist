import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

# Replace CLIENT_ID and CLIENT_SECRET with your own values
CLIENT_ID = '<insert client id here>'
CLIENT_SECRET = '<insert client secret here>'
USER_ID = '<insert user id here>'

with open('page-source.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

links = [a['href'] for a in soup.find_all('a', href=True) if 'https://open.spotify.com' in a['href']]
print(links)

playlist_title = soup.find("h5").text
print(playlist_title)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-modify-public"))

playlist_response = sp.user_playlist_create(USER_ID, playlist_title)
print(playlist_response)
playlist_id = playlist_response["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=links)
