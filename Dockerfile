FROM python:3.11-slim

# install build tools
RUN apt-get update && apt-get install -y build-essential git minicom && rm -rf /var/lib/apt/lists/*
WORKDIR /workspaces/iot

# tooling
RUN pip install \
    esptool==4.7.0 \
    adafruit-ampy==1.1.0 \
    rshell \
    micropy-cli \
    micropython-esp32-stubs \
    black \
    micropython-esp32-stubs==1.26.0.post1

# setup a non-root user
RUN useradd -ms /bin/bash iot_user
USER iot_user
