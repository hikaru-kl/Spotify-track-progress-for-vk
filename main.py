import vk_api
import requests
import asyncio
import time

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
    while True:
        headers = {
            f"Authorization": "Bearer " + SPOTIFY_SECRET,
            "Content-Type": "application/json"
        }
        r = requests.get(
            route("/me/player/currently-playing"), headers=headers)
        data = r.json()
        song_name = data["item"]["name"]
        song_artist = data["item"]["artists"][0]["name"]
        progress = convert_time(data["progress_ms"]) + \
            "/" + convert_time(data["item"]["duration_ms"])
        song_uri = data["item"]["uri"].split(":")
        song_url = "https://{}.com/{}/{}".format(
            song_uri[0], song_uri[1], song_uri[2])
        status = f"Слушает: {song_artist} - {song_name} {progress}\n\n{song_url}"
        vk_session.method("status.set", {"text": status})
        time.sleep(31)

if __name__ == '__main__':
    asyncio.run(main())
