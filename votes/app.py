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


if __name__ == "__main__":
    app.run()

