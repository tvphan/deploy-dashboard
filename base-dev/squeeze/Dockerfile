# Dockerfile for jenkins slave

FROM debian:squeeze
MAINTAINER Cloudant, An IBM Company <support@cloudant.com>
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp

# Don't use the frequently broken "smart" mirrors
RUN sed -i s/http.debian.net/ftp.uk.debian.org/g /etc/apt/sources.list

RUN apt-get -qq update && \
    apt-get install -qq -y --no-install-recommends \
	apt-utils \
    autoconf \
    automake \
    build-essential \
    curl \
    git \
    libncurses5-dev \
    libssl-dev \
    libtool \
    libz-dev \
	libnspr4-dev \
	libicu-dev \
	libpcre3 \
	libpcre3-dev \
	libssl-dev \
	python \
	python-pip \
	python-setuptools \
	rsync \
	ruby-dev \
	rubygems \
	s3cmd \
	subversion \
	sudo \
    tar \
    unzip \
    vim \
    wget

RUN wget -q http://packages.cloudant.com/debian/dists/squeeze/main/binary-amd64/libmozjs185-cloudant_1.8.5-cloudant1_amd64.deb && \
    wget -q http://packages.cloudant.com/debian/dists/squeeze/main/binary-amd64/libmozjs185-cloudant-dev_1.8.5-cloudant1_amd64.deb && \
    dpkg -i -R /tmp/libmozjs185*

RUN wget -q http://www.erlang.org/download/otp_src_17.1.tar.gz && \
    tar -xvzf otp_src_17.1.tar.gz && \
    cd otp_src_17.1 && \
    ./configure \
        --enable-threads \
        --enable-smp-support \
        --enable-m64-build && \
    make && \
    make install

# Install python modules
RUN pip install -q jinja2 pyyaml

# Install a basic SSH server
RUN apt-get install -y openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# Install JDK
RUN apt-get install -y --no-install-recommends openjdk-6-jdk

# Install fpm
RUN gem install fpm
RUN ln -s /var/lib/gems/1.8/bin/fpm /usr/local/bin

# Install rebar from github
RUN curl -L https://github.com/rebar/rebar/wiki/rebar > /usr/local/bin/rebar \
	&& chmod +rx /usr/local/bin/rebar

RUN cd /opt && \
	wget -q http://mirror.metrocast.net/apache/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz && \
    tar -xvf apache-maven-3.2.5-bin.tar.gz && \
    echo "export M2_HOME=/opt/apache-maven-3.2.5" > /etc/profile.d/maven.sh && \
    echo "export M2=\$M2_HOME/bin" >> /etc/profile.d/maven.sh && \
    echo "export PATH=\$M2:\$PATH" >> /etc/profile.d/maven.sh && \
    rm apache-maven-3.2.5-bin.tar.gz && \
    ln -s /opt/apache-maven-3.2.5/bin/mvn /usr/local/bin

ONBUILD workdir /tmp
ONBUILD EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
