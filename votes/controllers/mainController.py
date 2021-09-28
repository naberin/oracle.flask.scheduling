from flask import jsonify


class MainController:

    @staticmethod
    def health():
        return jsonify({"status": "UP"}), 200


