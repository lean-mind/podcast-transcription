FROM python:3.10

WORKDIR /app

COPY ./ ./

RUN apt-get -y update
RUN apt-get install -y make
RUN pip install pipenv
RUN make setup-docker
RUN cd /app mkdir audio_mp3_folder audio_text_folder mp4_folder