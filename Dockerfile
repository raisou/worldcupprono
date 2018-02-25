FROM ubuntu:16.04
MAINTAINER Fabien Loffredo <contact@fabienloffredo.com>

# We dont want buffer for stdin, stdout et stderr.
ENV PYTHONUNBUFFERED 1

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    gcc \
    libpq-dev \
    locales \
    openssh-client \
    python3.6 \
    python3.6-dev \
    python3-pip \
    python3-virtualenv \
    python-setuptools \
    python3-setuptools \
    vim \
    virtualenv \
    && apt-get autoremove \
    && apt-get clean

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# add NodeSource repository for Node.js 8.0
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# We install requirements
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
