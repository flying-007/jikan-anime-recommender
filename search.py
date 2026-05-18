import requests
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


while True:
    x = input("Search anime/characters/manga/people/producers: ").lower()

    if x not in ["anime", "characters", "manga", "people", "producers"]:
        print("Invalid category")
        continue

    y = input(f"What {x} do you want to search? ")

    time.sleep(1)

    result = api_get(
        f"{BASE_URL}/{x}",
        {"q": y, "limit": 5}
    )

    data = result.get("data", [])

    print(f"\nTotal results: {len(data)}\n")

    for i, item in enumerate(data, start=1):

        print("=" * 50)

        if x == "anime":
            print(i, item.get("title"))
            print("Score:", item.get("score"))
            print("Episodes:", item.get("episodes"))
            print("Synopsis:", item.get("synopsis"))

        elif x == "manga":
            print(i, item.get("title"))
            print("Score:", item.get("score"))
            print("Chapters:", item.get("chapters"))
            print("Synopsis:", item.get("synopsis"))

        else:
            print(i, item.get("name"))
            print("Favorites:", item.get("favorites"))

    back = input("\nBack to main menu? (yes/no): ").lower()

    if back == "yes":
        break
