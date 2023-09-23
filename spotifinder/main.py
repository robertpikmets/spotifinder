import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        redirect_uri="http://localhost:8000",
        scope="user-library-read",
    )
)

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results["items"]):
    track = item["track"]
    print(idx, track["artists"][0]["name"], " - ", track["name"])
