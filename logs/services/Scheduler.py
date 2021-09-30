from flask_apscheduler import APScheduler


class Config:
    SCHEDULER_API_ENABLED = True


class Scheduler:
    def __init__(self, app):
        self.scheduler = APScheduler()
        self.scheduler.init_app(app)

    def get(self):
        return self.scheduler

    def start(self):
        self.scheduler.start()
