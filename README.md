docker-images
=============

Docker files for development, test and production use. The docker files are grouped into the following categories

* base - Base dockerfiles. Just common and very basic packages.
* jenkins-base - Jenkins basic dockerfiles including SSH + 'jenkins' user configuration.
* base-local - Base development dockerfiles for Cloudant Local.
* jenkins-local - Jenkins specific dockerfiles for Cloudant Local.
* jenkins-dind - Jenkins specific dockerfiles for running jenkins slaves that can run docker inside of them aka DIND.

Getting Started
===============

1) Clone this repository locally
```bash
cd ~
git clone git@github.com:cloudant/docker-images
```

2) Install python dependencies in your virtualenv:
```bash
pip install -r requirements.txt
```

3) As SUDO or ROOT, create the following directories

	mkdir /srv
	mkdir /srv/builds

Then make them readable and writable to the world

	chmod go+rw /srv
	chmod go+rw /srv/builds

4) Configure the docker-images project:

	cd ~/docker-images
	./configure

5) Building the images
```bash

	cd ~/docker-images
	make

Alternately, to capture the output:

	make 2>&1 | tee ../make.log

```
