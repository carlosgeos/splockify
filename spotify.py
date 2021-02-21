import os
import requests

SPOTIFY_REFRESH_TOKEN = os.environ["SPOTIFY_REFRESH_TOKEN"]
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]


def get_spotify_access_token():
    """Returns a Spotify OAuth token (valid for 1 hr)

    """
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "refresh_token", "refresh_token": SPOTIFY_REFRESH_TOKEN}
    res = requests.post(url, data=data, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)).json()
    return res["access_token"]


def get_current_track(token):
    """Returns the raw respose to the currently-playing endpoint

    """
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(url, headers=headers)
    return res


def get_track_info():
    """Returns a dict with the currently playing song name and artist(s)
    name(s), if there is a song currently playing.

    Otherwise, returns False

    """
    res = get_current_track(get_spotify_access_token())
    if res.status_code == 204 or res.json()["is_playing"] is False:
        # When the song hasn't been playing for a while, the status
        # code is simply 204 and there is no body. Otherwise,
        # is_playing will be false
        return False
    else:
        track = res.json()
        return {
            "track_name": track["item"]["name"],
            "artist_name": ", ".join(list(map(lambda i: i["name"], track["item"]["artists"])))
        }
