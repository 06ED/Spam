import requests

ACCESS_TOKEN = ""
VERSION = "5.131"
TIME = 5
USERS_ID = []

with open("users.txt", "r", encoding="utf-8") as file:
    for _id in file.read().split("\n"):
        if _id.startswith("id"):
            USERS_ID.append(int(_id[2:]))
        else:
            request = requests.get(url="https://api.vk.com/method/users.get", params={
                "access_token": ACCESS_TOKEN,
                "v": VERSION,
                "user_ids": _id,
            })
            USERS_ID.append(request.json()["response"][0]["id"])
