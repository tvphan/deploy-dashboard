# Dockerfile for base centos development image 

FROM centos:centos6

MAINTAINER Cloudant, An IBM Company <support@cloudant.com>

# First install wget so we can install 3rd party repositories
RUN yum -q -y install wget

# Enable EPEL repository
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# Install erlang
RUN wget http://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm \
    && rpm -Uvh erlang-solutions-1.0-1.noarch.rpm \
    && rm erlang-solutions-1.0-1.noarch.rpm \
    && yum clean all

ENV ERLANG_VERSION 17.1-1
RUN yum install -y esl-erlang-$ERLANG_VERSION.x86_64

# Install prereqs
RUN yum -q -y groupinstall "Development tools"
RUN yum -q -y install \
    autoconf213 \
    autoconf \
    bzip2 \
    createrepo \
    curl \
    expect \
    install \
    file \
    gcc \
    gcc-c++ \
    git \
	glibc-devel \
    glibc-static \
    java-1.6.0-openjdk-devel \
	js-devel \
	libicu-devel \
    libtool \
    make \
    ncurses-devel \ 
    nspr-devel \
    openssh-server \
    openssl \
	openssl-devel \
    passwd \
	pcre \
	pcre-devel \
	python-pip \
	python-setuptools \
	readline-devel \
    redhat-rpm-config \
    rpmdevtools \ 
    rpm-build \ 
    ruby \
    ruby-devel \
    rubygems \
    rsyslog \
	s3cmd \
    screen \
    subversion \
    sudo \
    tar \
    which

RUN yum -q clean all \
    && libtool --finish /usr/lib

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

# Install rebar from github
RUN curl -L https://github.com/rebar/rebar/wiki/rebar > /usr/local/bin/rebar
RUN chmod +rx /usr/local/bin/rebar

RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd
RUN /etc/init.d/sshd restart

# Install the python modules
RUN pip -q install jinja2 pyyaml

Disable IPv6
RUN sysctl -w net.ipv6.conf.all.disable_ipv6=1
RUN sysctl -w net.ipv6.conf.default.disable_ipv6=1

CMD ["/usr/sbin/sshd", "-D"]

# Defer following to child images 
ONBUILD EXPOSE 22
ONBUILD WORKDIR /tmp 
