import requests
from typing import Any

class SteamAPI:
    # APPID IS REQUIRED! 
    # Mandatory (After first page): "cursor={cursorid}"
    # Optional: "json"=1
    REVIEW = "https://store.steampowered.com/appreviews/"

    # APPID IS REQUIRED! 
    # Optional: "count_before"=0, "count_after"=100000
    PATCH = "https://store.steampowered.com/events/ajaxgetadjacentpartnerevents/"

    # APPIDS IS REQUIRED! 
    # Optional: "filters=genres", "cc=us", "l=english"
    GAME_DETAILS = "https://store.steampowered.com/api/appdetails"

    # API KEY AND USERID ARE REQUIRED!
    # Optional: "format=json", "include_appinfo=True", "include_played_free_games=True"
    USER_GAMES = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

    # APPID IS REQUIRED! IT SHOULD BE FILLED DIRECTLY IN URL.
    # Optional:"l=english"
    GAME_RATING_HISTORY = "https://store.steampowered.com/appreviewhistogram/{appid}"

        

class APITools:
    def fetch_data(parameters: dict[str, Any], 
                   id_list: list[str],
                   id_type: str,
                   url: str,
                   key: str | None = None,
                   direct_fill: dict[str, bool] = {"None": ["None", False]}
                   ) -> dict[str, dict[str, Any]]:
        
        data: dict[str, dict[str, Any]] = {}

        if key is not None:
            parameters["key"] = key

        if direct_fill["None"][1]:
            url = url.format(appid=direct_fill["None"][0])


        with requests.session() as session:
            try:
                for id in id_list:
                    if not direct_fill["None"][1]:
                        parameters[id_type] = id

                    connection_status = session.get(url, params=parameters, timeout=5)
                    connection_status.raise_for_status()

                    json_received = connection_status.json()
                    data[id] = json_received

            except requests.exceptions.Timeout:
                print("Request Timed out1")

        return data




        














