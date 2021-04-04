print("Running imports")
import os
import requests
import json
import datetime

import os

if not os.path.exists("json"):
    os.makedirs("json")

USER, PASSWORD = "", ""
TIME_STAMP = datetime.datetime.now().strftime("%m%d%Y-%H%M")

print("Running definitions")
# Define global variables

LOGIN_URL = "https://web.bestcoastpairings.com/login.php"

ROOT = "https://lrs9glzzsf.execute-api.us-east-1.amazonaws.com/prod/"
EVENT_URL, PAIRING_URL = [ROOT + i for i in ("eventlistings", "pairings")]

KEEP_KEYS = [
    "pairingTable",
    "pairingType",
    "isDone",
    "objectId",
    "createdAt",
    "updatedAt",
    "eventId",
    "table",
    "round",
    "isActiveUser",
    "isPlayer",
    "gameSystemId",
    "scorecardId",
    "metaData",
    "player1",
    "player2",
]

print("Session login")
# Session login
session = requests.session()
login_data = {"USERNAME": USER, "PASSWORD": PASSWORD}
r = session.post(LOGIN_URL, data=login_data)

print("Pulling tournament data")
# Pull tournament data
params = {"startDate": "2020-01-01", "gameType": "1"}
events = session.get(EVENT_URL, params=params).json()

print(f"{len(events)} events found")

# Dump tournament data

print("Writing tournament data to file")
with open(f"json/tournaments_{TIME_STAMP}", "w") as f:
    json.dump(events, f)

# Pull games

games = []
for n, event in enumerate(events):
    print(f"Pulling tournament {n} of {len(events)}")

    params = {
        "eventId": event["eventObjId"],
        "inclScorecard": "true",
        "inclGameSystem": "false",
        "inclEvent": "false",
    }

    # Pull pairing data
    p = session.get(
        PAIRING_URL,
        params=params,
    )
    if p.status_code == 200:
        pairings = p.json()

        # Run through each pairing and drop to games
        for pairing in pairings:
            game = {i: pairing.get(i) for i in KEEP_KEYS}
            games.append(game)
    else:
        continue

# Dump games to file

print(f"All done, {len(games)} found")
with open(f"json/tournaments_{TIME_STAMP}", "w") as f:
    json.dump(games, f)
