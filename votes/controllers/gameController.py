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

    @staticmethod
    def list_games(c_page=1, limit=25):
        games = app.rds.lrange('games', (c_page-1)*limit, end=c_page*limit)
        next_games = app.rds.lrange('games', c_page*limit+1, end=(c_page+1)*limit)

        list_of_games = [g.decode('UTF-8') for g in games]

        return jsonify({
            "games": list_of_games,
            "count": len(list_of_games),
            "has_next":  len(next_games) > 0,
            "page": c_page
        }), 200


