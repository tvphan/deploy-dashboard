# Dockerfile for generating base image

FROM ubuntu:12.04
MAINTAINER Cloudant, An IBM Company <support@cloudant.com>
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp

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
    openssh-server \
    less

# Configure SSH server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

ONBUILD workdir /tmp
ONBUILD EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
