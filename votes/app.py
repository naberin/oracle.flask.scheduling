from flask import Flask, request
from controllers.mainController import MainController
from config.constants import Constants

import redis

app = Flask(__name__)
rds = redis.Redis(host=Constants.REDIS_HOST, port=Constants.REDIS_PORT, db=0)


@app.route("/api/health")
def health():
    return MainController.health()


if __name__ == "__main__":
    app.run()

