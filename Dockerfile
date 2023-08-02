# FROM python3.9
FROM python:3.8-slim-buster

WORKDIR /app
EXPOSE 8888
EXPOSE 80

COPY ./src .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--bind=0.0.0.0:8888", "wsgi:app"]
