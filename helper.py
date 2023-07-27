import requests


# checks if hypixel gamemode, paintball, has enough players to start game
def check_if_starting():
    data = requests.get(
        url="https://api.hypixel.net/gameCounts?",
        params={
            "key": "HYPIXEL_API_KEY"
        }
    ).json()

    pb_player_count = data['games']['LEGACY']['modes']['PAINTBALL']

    if pb_player_count > 7:
        return "Game has enough players to start"
    return "Game does not have enough players to start"
