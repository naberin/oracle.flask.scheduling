from flask import Flask, request
from controllers.mainController import MainController
from controllers.gameController import GameController
from config.constants import Constants

import redis

app = Flask(__name__)
rds = redis.Redis(host=Constants.REDIS_HOST, port=Constants.REDIS_PORT, db=0)

rds.set("games:id", 1000)


@app.route("/api/health")
def health():
    return MainController.health()


@app.route("/api/games", methods=["GET", "POST"])
def games():

    if request.method == "POST":
        return GameController.create_game()

    elif request.method == "GET":
        return GameController.list_games()


@app.route("/api/games/<game_id>", methods=["GET", "PUT"])
def manage_game_with(game_id):

    if request.method == "GET":
        return GameController.get_game_with(game_id=game_id)

    elif request.method == "PUT":

        if request.json and "team" in request.json:
            team = request.json["team"]
            return GameController.put_point(game_id=game_id, team=team)
        else:
            return GameController.err_400_body_not_found()


if __name__ == "__main__":
    app.run()

