# Using Flask-APScheduler
Scheduling Jobs using Flask-APScheduler.

# Getting Started (Locally)
First install the packages required
```bash
pip install -r requirements.txt
```
Then, run the Flask app server.
```bash
flask run
```

# Getting Started (Dockerized)
Without `docker-compose`
```bash
docker build -t logs:latest .
docker run -p 5000:5000 logs:latest
```
With `docker-compose`
```bash
docker-compose up --build
```