FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    apt-utils \
    wget

RUN apt-get install -y python-is-python3
RUN apt-get install -y  python3-pip

EXPOSE 8888
EXPOSE 80

COPY ./src .

RUN pip install -r requirements.txt

CMD ["python", "application.py"]
