import requests
import random
import time

BASE_URL = "https://api.jikan.moe/v4"


def api_get(url, params=None):
    while True:
        response = requests.get(url, params=params)

        if response.status_code == 429:
            print("Rate limit reached. Waiting 2 seconds...")
            time.sleep(2)
            continue

        response.raise_for_status()
        return response.json()


def show_anime(a):
    print("\n" + "=" * 50)
    print("Title:", a.get("title"))
    print("Score:", a.get("score"))
    print("Episodes:", a.get("episodes"))
    print("Rank:", a.get("rank"))
    print("Synopsis:", a.get("synopsis"))


def show_manga(m):
    print("\n" + "=" * 50)
    print("Title:", m.get("title"))
    print("Score:", m.get("score"))
    print("Chapters:", m.get("chapters"))
    print("Rank:", m.get("rank"))
    print("Synopsis:", m.get("synopsis"))


while True:

    mode = input(
        "Random or personalized recommendation? "
    ).lower()

    if mode == "random":

        category = input(
            "anime/manga/characters/people: "
        ).lower()

        time.sleep(1)

        result = api_get(
            f"{BASE_URL}/random/{category}"
        )

        data = result["data"]

        if category == "anime":
            show_anime(data)

        elif category == "manga":
            show_manga(data)

        else:
            print("Name:", data.get("name"))
            print("Favorites:", data.get("favorites"))
            print("About:", data.get("about"))

    elif mode == "personalized":

        category = input("anime or manga: ").lower()

        genre = input(
            "Genre (Action/Comedy/etc or none): "
        )

        minimum_score = input(
            "Minimum score out of 10 (or none): "
        )

        params = {"limit": 20}

        if minimum_score.lower() != "none":
            params["min_score"] = float(minimum_score)

        time.sleep(1)

        result = api_get(
            f"{BASE_URL}/{category}",
            params
        )

        data = result["data"]

        if genre.lower() != "none":
            filtered = []

            for item in data:
                genres = [
                    g["name"].lower()
                    for g in item.get("genres", [])
                ]

                if genre.lower() in genres:
                    filtered.append(item)

            data = filtered

        if len(data) == 0:
            print("No recommendations found")
            continue

        random.shuffle(data)

        for item in data[:5]:

            if category == "anime":
                show_anime(item)

            else:
                show_manga(item)

            another = input(
                "\nAnother recommendation? (yes/no): "
            ).lower()

            if another == "no":
                break

    else:
        print("Invalid input")

    back = input(
        "\nBack to main menu? (yes/no): "
    ).lower()

    if back == "yes":
        break
