# WIP do not use
FROM nvidia/cuda:12.0.0-base-ubuntu20.04
CMD nvidia-smi
RUN apt-get update && apt-get install -y python3.10 make ffmpeg
RUN python -m pip install -U pip

WORKDIR /app

COPY ./ ./

RUN pip install pipenv
RUN make setup-docker