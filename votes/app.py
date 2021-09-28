from flask import Flask, request
from controllers.mainController import MainController

app = Flask(__name__)


@app.route("/api/health")
def health():
    return MainController.health()


if __name__ == "__main__":
    app.run()

