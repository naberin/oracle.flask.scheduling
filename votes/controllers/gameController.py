from config.constants import Constants
from flask import jsonify
import app


class GameController:

    @staticmethod
    def create_game():
        game_id = app.rds.incr("games:id")
        app.rds.lpush('games', f'G{game_id}')
        app.rds.hset(f'G{game_id}', Constants.TEAM_ONE, 0)
        app.rds.hset(f'G{game_id}', Constants.TEAM_TWO, 0)

        return jsonify({"id": f'G{game_id}'}), 200

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

    @staticmethod
    def get_game_with(game_id):
        score_team_1 = app.rds.hget(game_id, Constants.TEAM_ONE)
        score_team_2 = app.rds.hget(game_id, Constants.TEAM_TWO)

        if score_team_1 and score_team_2:
            score_1 = score_team_1.decode('UTF-8')
            score_2 = score_team_2.decode('UTF-8')

            return jsonify({
                Constants.TEAM_ONE: int(score_1),
                Constants.TEAM_TWO: int(score_2),
            }), 200

        else:
            return GameController.err_404_game()


    @staticmethod
    def err_404_game():
        return jsonify({"error": f"game not found"}), 404
