FROM ubuntu:groovy

# set a directory for the app
WORKDIR /root

# copy all the files to the container
COPY . .

# install ubuntu package
RUN export TZ=Europe/Paris
ARG DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && apt-get install -y \
  alsa-utils \
  tzdata \
  python3.8 \
  python-numpy \
  ffmpeg \
  build-essential \
  libssl-dev \
  libffi-dev \
  python3-dev \
  libcairo2-dev \
  libgirepository1.0-dev \
  libsdl-image1.2-dev \
  libsdl-mixer1.2-dev \
  libsdl-ttf2.0-dev \
  libsmpeg-dev \
  libsdl1.2-dev \
  libportmidi-dev \
  libswscale-dev \
  libavformat-dev \
  libavcodec-dev \
  libfreetype6-dev \
  python-setuptools \
  python3-pip

# install python libraries
RUN pip3 install -r requirements.txt
