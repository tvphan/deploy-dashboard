# Dockerfile for jenkins centos7 slave 

FROM centos:centos7

MAINTAINER Cloudant, An IBM Company <support@cloudant.com>

# Enviroment Variables
ENV USERNAME=jenkins \
    PASSWORD=jenkins \
    GROUP=jenkins \
    HOME=/home/jenkins \
    ERLANG_VERSION=17.5.6.5

# Set up a user for builds
RUN adduser -d $HOME $USERNAME \
    && echo "${USERNAME}:${GROUP}" | chpasswd \

# Enable EPEL and Erlang repositories
    && yum install -q -y deltarpm wget epel-release \
    && wget -q http://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm \
    && rpm -Uvh erlang-solutions-1.0-1.noarch.rpm \
    && rm erlang-solutions-1.0-1.noarch.rpm \

# Install remainder of the prereq packages
    && yum install -q -y \
    autoconf213 \
    autoconf \
    bzip2 \
    createrepo \
    esl-erlang-$ERLANG_VERSION.x86_64 \
    expect \
    install \
    gcc \
    gcc-c++ \
    git \
    glibc-devel \
    glibc-static \
    java-1.6.0-openjdk-devel \
    js-devel \
    libtool \
    make \
    ncurses-devel \
    nspr-devel \
    openssh-server \
    openssl \
    openssl-devel \
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
    which \

# Install JRE1.7 and make it the default java runtime
    java-1.7.0-openjdk

RUN yum -q clean all \
    && libtool --quiet --finish /usr/lib \

# Install maven
    && cd /tmp \
    && wget -q http://apache.osuosl.org/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz \
    && mkdir /usr/local/apache-maven \
    && cd /usr/local/apache-maven \
    && tar -xzf /tmp/apache-maven-3.2.5-bin.tar.gz \
    && echo "export M2_HOME=/usr/local/apache-maven/apache-maven-3.2.5" > /etc/profile.d/maven.sh \
    && echo "export M2=\$M2_HOME/bin" >> /etc/profile.d/maven.sh \
    && echo "export PATH=\$M2:\$PATH" >> /etc/profile.d/maven.sh \
    && ln -s /usr/local/apache-maven/apache-maven-3.2.5/bin/mvn /usr/local/bin/mvn \

# Install rebar from github
    && curl --silent -L https://github.com/rebar/rebar/wiki/rebar > /usr/local/bin/rebar \
    && chmod +rx /usr/local/bin/rebar \

# Setup ssh 
    && ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' \
    && sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g' /etc/pam.d/sshd \
    && mkdir -p /var/run/sshd \

# Install the python modules
    && pip -q install jinja2 pyyaml \

# Enable the Cloudant Local External Dependencies Repository 
    && cd /etc/yum.repos.d \
    && wget -q http://s3.amazonaws.com/cloudant-local/redhat/cloudant-local-extdeps.repo \

# Install FPM
    && gem install -q cabin -v 0.7.2 \
    && gem install -q fpm

# Configure git
ADD shared/gitconfig $HOME/.gitconfig
RUN chown ${USERNAME}:${GROUP} $HOME/.gitconfig \
    && git config --global url."git@github.com:".insteadOf git://github.com/ \
    && git config --global url."git@github.com:".insteadOf https://github.com

# Configure maven
RUN mkdir -p $HOME/.m2
ADD shared/settings.xml $HOME/.m2/settings.xml
RUN chown -R ${USERNAME}:${GROUP} $HOME/.m2

# Configure ssh login
RUN mkdir -p $HOME/.ssh
ADD shared/id_rsa $HOME/.ssh/id_rsa
ADD shared/ssh_config $HOME/.ssh/config

RUN chown -R ${USERNAME}:${GROUP} $HOME/.ssh \
    && chmod -R og-rwx $HOME/.ssh

# Grant the user sudo privileges
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD:   ALL" >> /etc/sudoers \
    && echo "Defaults!/usr/bin/yum !requiretty" >> /etc/sudoers

# Setup AWS s3cmd tool
ADD shared/s3cfg $HOME/.s3cfg
RUN chown -R ${USERNAME}:${GROUP} $HOME/.s3cfg

# Expose port 22 
EXPOSE 22
WORKDIR /tmp

# Disable root password
RUN passwd -l root

CMD ["/usr/sbin/sshd", "-D"]
