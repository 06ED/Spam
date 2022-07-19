import time
import settings
import requests
from random import getrandbits, choice, randint


def get_random_id() -> int:
    return getrandbits(31) * choice([-1, 1])


def get_message() -> str:
    with open("message.txt", "r", encoding="utf-8") as file:
        return file.read()


def is_friend(user_id: int, token: str, version: str) -> bool:
    request = requests.get(url="https://api.vk.com/method/friends.areFriends", params={
        "access_token": token,
        "v": version,
        "user_ids": str(user_id)
    })
    return True if request.json()["response"][0]["friend_status"] == 3 else False


def add_friend(user_id: str, version: str, token: str) -> None:
    request = requests.get(url="https://api.vk.com/method/friends.add", params={
        "access_token": token,
        "v": version,
        "user_id": user_id
    })
    print(request.json())


def send_message(user_id: int, token: str, message: str, version: str) -> None:
    request = requests.get(url="https://api.vk.com/method/messages.send", params={
        "access_token": token,
        "v": version,
        "user_id": user_id,
        "random_id": get_random_id(),
        "message": message
    })
    print(request.json())


def add_like(user_id: int, photo_id: int, token: str, version: str) -> None:
    request = requests.get(url="https://api.vk.com/method/likes.add", params={
        "access_token": token,
        "v": version,
        "owner_id": user_id,
        "item_id": photo_id,
        "type": "photo"
    })
    print(request.json())


def get_photo_ids(user_id: int, token: str, version: str, count=10) -> list:
    to_return = []

    request = requests.get(url="https://api.vk.com/method/wall.get", params={
        "access_token": token,
        "v": version,
        "owner_id": user_id,
        "count": count,
        "filter": "owner",

    })
    print(request.json())

    for item in request.json()["response"]["items"]:
        try:
            for attachment in item["attachments"]:
                if attachment["type"] == "photo":
                    to_return.append(attachment["photo"]["id"])
        except KeyError:
            continue

    return to_return


def main():
    for _user_id in settings.USERS_ID:
        add_friend(user_id=_user_id, version=settings.VERSION, token=settings.ACCESS_TOKEN)
        photo_ids = get_photo_ids(user_id=_user_id, token=settings.ACCESS_TOKEN, version=settings.VERSION)
        for _photo_id in photo_ids:
            time.sleep(randint(10, 21))
            add_like(user_id=_user_id, photo_id=_photo_id,
                     token=settings.ACCESS_TOKEN, version=settings.VERSION)
        time.sleep(settings.TIME + randint(5, 12))
        send_message(user_id=_user_id, token=settings.ACCESS_TOKEN,
                     message=get_message(), version=settings.VERSION)


if __name__ == "__main__":
    main()
