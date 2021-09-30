import sys
import os
import logging
import redis

from datetime import datetime
from flask import Flask, jsonify
from services.Scheduler import Scheduler, Config

os.environ['TZ']= 'America/Chicago'
host = os.getenv('REDIS_HOST', 'localhost')

app = Flask(__name__)
app.config.from_object(Config())

rds = redis.StrictRedis(host=host, port=6379, db=0)

scheduler = Scheduler(app).get()
scheduler.start()


@app.route("/api/health")
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/api/timestamps")
def timestamps():
    length_of_timestamps = rds.llen("timestamps")
    list_of_timestamps = [times.decode('UTF-8') for times in rds.lrange("timestamps", 0, length_of_timestamps)]

    return jsonify({"data": list_of_timestamps, "count": length_of_timestamps}), 200


@scheduler.task('interval', id='print_job', minutes=1, misfire_grace_time=60)
def record():
    time = datetime.strftime(datetime.now(), '%b%d:%Y %H:%M:%S')
    rds.lpush('timestamps', time)
    print('Timestamp inserted', file=sys.stderr)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)

