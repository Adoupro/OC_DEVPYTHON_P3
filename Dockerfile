FROM ubuntu:latest

# set a directory for the app
WORKDIR /root

# copy all the files to the container
COPY . .

# install pygame & dependencies
RUN apt-get update && apt-get install -y \
  python3.8 \
  python3-numpy \
  libav-tools \
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
  python3-setuptools \
  python-pygame
