import requests
import random
import string
import json
import time

COLORS = {
    "RESET"  : "\u001b[0m",
    "Black"  : "\u001b[30m",
    "Red"    : "\u001b[31m",
    "Green"  : "\u001b[32m",
    "Yellow" : "\u001b[33m",
    "Blue"   : "\u001b[34m",
    "Magenta": "\u001b[35m",
    "Cyan"   : "\u001b[36m",
    "White"  : "\u001b[37m"
    }

TOKEN  = input(f"{COLORS['Green']}[~]{COLORS['RESET']} Webhook URL: ")
AMOUNT = int(input(f"{COLORS['Green']}[~]{COLORS['RESET']} Amount of messages to send: "))
message = input(f"{COLORS['Green']}[~]{COLORS['RESET']} Message: ")

#SPAM CHAT
# https://discord.com/api/webhooks/848722693716049930/hCnQLD7F5cHsHvQJl-z4vYikNijEztlPIbvDG1gP7KYJD1PBvGkz9QBwAMj1Lw3LI1rJ

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send(token, message):
    username = id_generator()
    if len(message) < 1:
        message = "@everyone " + id_generator(1900)
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": True
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(TOKEN, data, headers=header)
    print(f"{COLORS['Cyan']}Sending message!{COLORS['RESET']}")
    if not response.ok:
        if response.status_code == 429:
            print(f"{COLORS['Yellow']}Too many requests.. - waiting before retying..{COLORS['RESET']}")
            time.sleep(1)
        else:
            print(f"{COLORS['Red']}Failed to send message!{COLORS['RESET']}")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        return False
    else:
        print(f"{COLORS['Green']}Sent message!{COLORS['RESET']}")
        return True

for i in range(AMOUNT):
    send(TOKEN, message)
