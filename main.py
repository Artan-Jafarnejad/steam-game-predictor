from flask import Flask, render_template, request
from program.services import SteamGameServices, SteamUserService
from program.calculations import Calculation


server = Flask(__name__)


def rating(steamid: str,
           key: str,
           gameid: str) -> float:
    
    # fetch user's games, then calculating its tags scores
    user: object = SteamUserService(user_id=steamid, key=key)
    game_and_playtime: dict[str, float] = user.user_playtime_and_games()
    game_list: list[str] = [gameid for gameid in game_and_playtime.keys()]
    game: object = SteamGameServices(game_list)
    genres: dict[str, list[str]] = game.game_genre()
    score_list, total_score = Calculation.games_tag_score(genres, game_and_playtime)

    # fetching chosen game's tags
    target_tags: dict[str, list[str]] = SteamGameServices([gameid]).game_genre()

    # comparing and returning its final score
    score: float = Calculation.recommendation_rating(
        games_score=score_list,
        total_score=total_score,
        target_tags=target_tags
    )
    return round(score * 100, 2)


temporary: list[dict[str, str]] = [
    {
        "rating": "NOTE: After submitting, the request may take up few minutes."
    }
]

@server.route("/")
def main_page(score: list[dict[str, str]] | None = None):
    if score is None:
        return render_template("website.html", data=temporary)
    else:
        return render_template("website.html", data=score) 



@server.route("/data", methods=["POST"])
def show_score() -> list[dict[str, int]]:

    steamid: str = request.form.get("usernameid")
    key: str = request.form.get("key")
    gameid: str = request.form.get("gameid")

    score: float = rating(steamid=steamid, key=key, gameid=gameid)

    data: list[dict[str, str]] = [
        {
            'rating': f"There is {score}% chance that you may like this game"
        }
    ]

    return main_page(data)


if __name__ == "__main__":
    server.run()
