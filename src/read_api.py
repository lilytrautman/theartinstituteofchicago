import json
import datetime
from pathlib import Path

import requests


def get_art_data(artwork_id):
    url = f"https://api.artic.edu/api/v1/artworks/{artwork_id}"
    params = {"fields": "id,title,artist_display,date_display"}
    response = requests.get(url, params=params)
    response.raise_for_status()

    timestamp = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S")
    data = response.json()
    Path("data").mkdir(exist_ok=True)
    with open(f"data/art_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

    Path("logs").mkdir(exist_ok=True)
    with open("logs/art.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} - Fetched art data for {artwork_id}\n")

    return data


if __name__ == "__main__":
    artwork = get_art_data(129884)
    print(json.dumps(artwork, indent=2))
