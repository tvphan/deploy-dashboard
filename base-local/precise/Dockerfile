# Dockerfile for generating base development image

FROM ubuntu:12.04
MAINTAINER Cloudant, An IBM Company <support@cloudant.com>
ENV DEBIAN_FRONTEND noninteractive

# Install erlang from external repo
RUN apt-get -qq update \
    && apt-get -qq install -y --force-yes apt-utils \
    && apt-get -qq install -y --force-yes wget ca-certificates \
    && wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
    && dpkg -i erlang-solutions_1.0_all.deb \
    && rm erlang-solutions_1.0_all.deb \
    && apt-get -qq update

ENV ERLANG_VERSION 1:17.1
RUN apt-get install -y --force-yes \
    erlang-base=$ERLANG_VERSION \
    erlang-asn1=$ERLANG_VERSION \
    erlang-crypto=$ERLANG_VERSION \
    erlang-dev=$ERLANG_VERSION \
    erlang-eldap=$ERLANG_VERSION \
    erlang-eunit=$ERLANG_VERSION \
    erlang-inets=$ERLANG_VERSION \
    erlang-os-mon=$ERLANG_VERSION \
    erlang-reltool=$ERLANG_VERSION \
    erlang-runtime-tools=$ERLANG_VERSION \
    erlang-ssh=$ERLANG_VERSION \
    erlang-syntax-tools=$ERLANG_VERSION \
    erlang-tools=$ERLANG_VERSION \
    erlang-xmerl=$ERLANG_VERSION \
    erlang-mnesia=$ERLANG_VERSION \
    erlang-ssl=$ERLANG_VERSION \
    erlang-snmp=$ERLANG_VERSION \
    erlang-wx=$ERLANG_VERSION \
    erlang-public-key=$ERLANG_VERSION \
    erlang-webtool=$ERLANG_VERSION

# Install build prereqs from standard repo
RUN apt-get -qq install -y --force-yes --no-install-recommends \
    build-essential \
    curl \
    libtool \
    autoconf \
    automake \
    git \
    ruby \
    ruby1.8-dev \
    rubygems \
    ssh \
    libopenssl-ruby1.8 \
    git \
    python-dev \
    python-pip \
    s3cmd \
    subversion \
    unzip \
    wget \
    sudo  \
    openjdk-6-jdk \
    libxml2-dev \
    libxslt-dev \
    libcurl4-openssl-dev \
    libmozjs185-dev \
    libpcre3 \
    libpcre3-dev \
    libssl-dev \
    libssl1.0.0 \
    libsnappy1 \
    libtool \
    libyaml-dev \
    vim

# Install maven
RUN cd /tmp \
    && wget -q http://apache.osuosl.org/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz \
    && mkdir /usr/local/apache-maven \
    && cd /usr/local/apache-maven \
    && tar -xzf /tmp/apache-maven-3.2.5-bin.tar.gz \
    && echo "export M2_HOME=/usr/local/apache-maven/apache-maven-3.2.5" > /etc/profile.d/maven.sh \
    && echo "export M2=\$M2_HOME/bin" >> /etc/profile.d/maven.sh \
    && echo "export PATH=\$M2:\$PATH" >> /etc/profile.d/maven.sh \
    && ln -s /usr/local/apache-maven/apache-maven-3.2.5/bin/mvn /usr/local/bin/mvn

ENV M2_HOME /usr/local/apache-maven/apache-maven-3.2.5

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install rebar from github
RUN curl -s -L https://github.com/rebar/rebar/wiki/rebar > /usr/local/bin/rebar
RUN chmod +rx /usr/local/bin/rebar

# Setup a basic SSH server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Need to install the 0.7.2 version of the cabin gem that FPM depends on to address FB ticket 58823 
RUN gem install cabin -v 0.7.2

#Install fpm. Need to pin it at 1.3.3 for this platform
RUN gem install fpm -v 1.3.3

# Install the python modules
RUN pip install -q jinja2 pyyaml

# Install python 2.7.10 as an alternative invokable with python2.7 
WORKDIR /tmp
RUN wget -O /tmp/Python-2.7.10.tar.xz https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz
RUN echo "c685ef0b8e9f27b5e3db5db12b268ac6  /tmp/Python-2.7.10.tar.xz" > /tmp/Python-2.7.10.tar.xz.md5 && md5sum --check /tmp/Python-2.7.10.tar.xz.md5
RUN tar xf /tmp/Python-2.7.10.tar.xz && cd /tmp/Python-2.7.10 && sudo ./configure && sudo make altinstall && rm /tmp/Python-2.7.10.tar.xz && rm /tmp/Python-2.7.10.tar.xz.md5
WORKDIR /
RUN sudo rm -rf /tmp/Python-2.7.10

RUN apt-get -qq purge

# Nightwatch related install
# Install nodejs & npm, firefox & virtual framebuffer
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get install -y --force-yes --no-install-recommends \
    nodejs firefox xvfb

# Use npm to install Nightwatch globally in /usr/lib/node_modules/nightwatch
RUN sudo npm install -g nightwatch

# Use wget to download selenium stand-alone server
RUN sudo wget http://selenium-release.storage.googleapis.com/2.48/selenium-server-standalone-2.48.0.jar
RUN sudo mv selenium-server-standalone-2.48.0.jar /usr/src
RUN chmod +x /usr/src/selenium-server-standalone-2.48.0.jar

# Set the DISPLAY environment variable used with Virtual framebuffer
ENV DISPLAY :0

# Standard SSH port
ONBUILD EXPOSE 22
ONBUILD WORKDIR /tmp

CMD ["/usr/sbin/sshd", "-D"]
