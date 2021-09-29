from celery import Celery


class CeleryApp:

    def __init__(self, app):
        self.celery = Celery(
            app.import_name,
            backend=app.config['RESULT_BACKEND'],
            broker=app.config['CELERY_BROKER_URL']
        )

        self.celery.conf.update(app.config)

        class ContextTask(self.celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        self.celery.Task = ContextTask

    def get(self):
        return self.celery
