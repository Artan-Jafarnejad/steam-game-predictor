# Self-Made Modules
from program.api import SteamAPI, APITools

# Python's Library
from typing import Any


class SteamGameServices:
    def __init__(self, app_id: int | list[str]):
        self.app_id = app_id


        
    def game_update_finder(self) -> int:
        parameters: dict[str, Any] = {
            "appid": self.app_id,
            "count_before": 0,
            "count_after": 100000
        }

        data: dict[str, dict[str, Any]] = APITools.fetch_data(
            parameters = parameters,
            id_list = [self.app_id],
            id_type = "appid",
            url = SteamAPI.PATCH
        )

        update_time: int = 0    # It will be in UNIX timestamp

        for latest_update in data[self.app_id]["events"]:
            if latest_update["event_type"] == 12 or latest_update["event_type"] == 13:
                update_time = latest_update["rtime32_start_time"]
                break

        return update_time



    def game_rating(self, 
                    update_time: int | None = None,
                    overall_rating: bool = False,
                    monthly_rating: bool = False,
                    update_rating: bool = False
                    ) -> float:
                    
        parameters: dict = {}
        data: dict[str, dict[str, Any]] = APITools.fetch_data(
            parameters = parameters,
            id_list = [self.app_id],
            id_type = "appid",
            url = SteamAPI.GAME_RATING_HISTORY,
            direct_fill = {"None": [self.app_id, True]}
        )

        update_pos: int = 0
        update_neg: int = 0
        month_pos: int = 0
        month_neg: int = 0
        overall_pos: int = 0
        overall_neg: int = 0


        for vote in data[self.app_id]["results"]["recent"]:
            if update_rating and vote["date"] > update_time:
                update_pos += vote["recommendations_up"]
                update_neg += vote["recommendations_down"]
            if monthly_rating:
                month_pos += vote["recommendations_up"]
                month_neg += vote["recommendations_down"]
        if overall_rating:
            for vote in data[self.app_id]["results"]["rollups"]:
                overall_pos += vote["recommendations_up"]
                overall_neg += vote["recommendations_down"]

        update_total: float = round((update_pos / (update_pos + update_neg)) * 100, 2)
        month_total: float = round((month_pos / (month_pos + month_neg)) * 100, 2)
        overall_total: float = round((overall_pos / (overall_pos + overall_neg)) * 100, 2)

        return update_total, month_total, overall_total



    def game_genre(self) -> dict[str, list[str]]:
        games_total_genres: dict[str, list] = {}
        parameters: dict[str, str] = {
            "filters": "genres",
            "cc": "us",
            "l": "english"
        }

        data: dict[str, dict[str, Any]] = APITools.fetch_data(
            parameters = parameters,
            id_list = self.app_id,
            id_type = "appids",
            url = SteamAPI.GAME_DETAILS
        )

        iteration: int = 0
        for game_json in data.values():
            current_id: str = self.app_id[iteration]
            app_success = game_json[current_id]["success"]
            app_genres_list = game_json[current_id].get("data")

            if not app_success or app_genres_list == []:
                iteration += 1
                continue

            for genre in app_genres_list["genres"]:
                games_total_genres.setdefault(current_id, []).append(genre["description"])

            iteration += 1
        return games_total_genres



class SteamUserService:
    def __init__(self, user_id: int, key: str):
        self.user_id = str(user_id)
        self.key = key



    def user_playtime_and_games(self) -> dict[str, float]:
        print(self.user_id)
        parameters: dict[str, Any] = {
            "steamid": self.user_id,
            "format": "json",
            "include_appinfo": True,
            "include_played_free_games": True
        }

        data: dict[str, dict[str, Any]] = APITools.fetch_data(
            parameters = parameters,
            id_list = [self.user_id],
            id_type = "steamid",
            url = SteamAPI.USER_GAMES,
            key = self.key
        )

        game_playtime: dict[str, int] = {}

        for game in data[self.user_id]["response"]["games"]:
            game_playtime[str(game["appid"])] = round(game["playtime_forever"] / 60, 2)

        return game_playtime






