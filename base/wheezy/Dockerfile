# Dockerfile for basic slave

FROM debian:wheezy
MAINTAINER Cloudant, An IBM Company <support@cloudant.com>
ENV DEBIAN_FRONTEND noninteractive

# Don't use the frequently broken "smart" mirrors
RUN sed -i s/http.debian.net/ftp.uk.debian.org/g /etc/apt/sources.list

RUN apt-get -qq update && \
    apt-get install -qq -y --no-install-recommends \
    autoconf \
    automake \
    build-essential \
    curl \
    git \
    python \
    python-pip \
    python-setuptools \
    rsync \
    rubygems \
    s3cmd \
    subversion \
    sudo \
    tar \
    unzip \
    vim \
    wget \
    less
