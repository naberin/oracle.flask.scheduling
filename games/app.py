import sys
import os
import redis

from flask import Flask, jsonify
from services.celery import CeleryApp

redis_host = os.getenv('REDIS_HOST', 'localhost')

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL=f'redis://{redis_host}:6379/0',
    RESULT_BACKEND=f'redis://{redis_host}:6379/0'
)
celery = CeleryApp(app).get()

rds = redis.Redis(host=redis_host, port=6379, db=0)
rds.set("games:id", 999)


@app.route("/api/health")
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/api/games", methods=["POST"])
def post_games():

    gid = _get_next_id()
    game_id = f"G{gid}"

    rds.lpush('games', game_id)
    return jsonify({"id": game_id}), 200


@app.route("/api/games", methods=["GET"])
def get_games():
    number_of_games = rds.llen('games')
    list_of_games = [g.decode('UTF-8') for g in rds.lrange('games', 0, number_of_games)]

    return jsonify({"games": list_of_games, "count": number_of_games}), 200


@celery.on_after_configure.connect()
def set_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, del_stale_games.s(), name='Delete Stale Games every 10 seconds')


def _get_next_id():
    return rds.incr("games:id")


@celery.task()
def del_stale_games():
    game_id = rds.rpop("games")
    print(f"Deleted: {game_id}", file=sys.stderr)
    if game_id:
        return game_id.decode('UTF-8')
    else:
        return None


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
