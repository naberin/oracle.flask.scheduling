from flask import jsonify
import app
import sys


class GameController:

    @staticmethod
    def create_game():
        game_id = app.rds.incr("games:id")
        app.rds.lpush('games', f'G{game_id}')
        app.rds.hset(f'G{game_id}', "team-1", 0)
        app.rds.hset(f'G{game_id}', "team-2", 0)

        return jsonify({"id": game_id}), 200


