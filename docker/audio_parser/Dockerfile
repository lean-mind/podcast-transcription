FROM python:3.10

WORKDIR /app

COPY ./ ./

RUN apt-get -y update
RUN apt-get install -y make ffmpeg
RUN pip install pipenv
RUN make setup-docker
