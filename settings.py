import requests

ACCESS_TOKEN = "vk1.a.GB5LQH5nuT1rNNC4e_5cbNdO18SpdhSiSVz-ZQ-9MBfoFkArBPAgsz8N" \
               "TmDQdoTdhMSoYb8mKxOEf_QXMTmGX2_OjpP5KhUnzWhd16ocpD-iDzKsO7Z2ML" \
               "XVuhCUC23inToCWFDNv1iCSxffwZphVGD3hDhQtMFV8CmLs_NW7VMy2XLRsSkY1-Ugjimr6Dc7"
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
