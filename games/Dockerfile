FROM python:alpine3.7

ENV REDIS_HOST=redis

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]