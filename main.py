import vk_api
import requests
import asyncio
import time
import random

ACCESS_TOKEN = open("vk_token.txt", "r").readlines()[0]
SPOTIFY_SECRET = open("spotify_token.txt", "r").readlines()[0]
BASE_URL = "https://api.spotify.com/v1"

vk_session = vk_api.VkApi(token=ACCESS_TOKEN)


def route(path):
    return BASE_URL + path


def convert_time(time_ms):
    minutes = time_ms // 60000
    seconds = time_ms % 60000 // 1000
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{minutes}:{seconds}"


async def main():
    global SPOTIFY_SECRET
    while True:
        headers = {
            f"Authorization": "Bearer " + SPOTIFY_SECRET,
            "Content-Type": "application/json"
        }
        r = requests.get(
            route("/me/player/currently-playing"), headers=headers)
        if 'application/json' in r.headers.get('Content-Type', ''):
            data = r.json()
        else:
            try:
                print(r.content)
            except Exception as exp:
                print(exp)
                exit()
            else:
                print({"error": "missing json content"})
                data = {"error": "missing json content"}
        if "error" not in data.keys():
            song_name = data["item"]["name"]
            song_artist = data["item"]["artists"][0]["name"]
            progress = convert_time(data["progress_ms"]) + \
                "/" + convert_time(data["item"]["duration_ms"])
            song_url = data["item"]["external_urls"]["spotify"]
            status = f"Слушает: {song_artist} - {song_name} {progress}\n\n{song_url}"
            vk_session.method("status.set", {"text": status})
        else:
            print(f"[ERROR] --> {data}")
            if isinstance(data["error"], dict) and data["error"]["status"] == 401:
                print("Trying to read new Spotify token..\nGet new token -> https://developer.spotify.com/console/get-users-currently-playing-track/")
                SPOTIFY_SECRET = open("spotify_token.txt", "r").readlines()[0]
        time.sleep(random.randint(25, 43))

if __name__ == '__main__':
    asyncio.run(main())
