# Oracle Flask Task Scheduling
Sample (and simple) apps running Flask and Redis (for Celery as a broker, but also as a data store)


### <code>games</code> - Celery example
The application provides the user APIs to create games and the app stores the IDs inside `redis`. With Celery, the app schedules the deletion of games that are stale after 30 seconds.

The following APIs are available:

```bash
# get a list of games
curl http://localhost:5000/api/games

# post a new game
curl -X POST http://localhost:5000/api/games
```


### <code>logs</code> - Flask-APScheduler example
The application provides the user an API to view a list of timestamps inserted into `redis` 

The following APIs are available:
```bash
# view a list of timestamps
curl http://localhost:5000/api/timestamps
```