# Using Celery
Scheduling Jobs using Celery.

# Getting Started (Locally)
First install the packages required
```bash
pip install -r requirements.txt
```
Then, run the Flask app server.
```bash
flask run
```
Then run a celery worker in the background
```bash
celery -A app.celery worker -l info
```
Finally, run Celery's beat scheduler
```bash
celery -A app.celery beat -l info
```

# Current Issues/Challenges
Dockerizing the celery worker and beat scheduler may be an issue and may need to be further explored