docker-images
=============

Docker files for development, test and production use. The docker files are grouped into the following categories

* base - Base dockerfiles. Just common and very basic packages.
* jenkins-base - Jenkins basic dockerfiles including SSH + 'jenkins' user configuration.
* base-local - Base development dockerfiles for Cloudant Local.
* jenkins-local - Jenkins specific dockerfiles for Cloudant Local.

NOTE: Extra steps have been added for building the Cloudant Local packages and
	  installer on the cloudubu64dk VM (managed by Rob Silvagni). These extra 
	  steps will be marked as "** Only Required for Cloudubu64dk **"

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

3) ** Only Required for Cloudubu64dk **
Add the following lines to the file ~/docker-images/configure in 
setup_deps() after the entry for .s3cfg:

	# The following file contains the github user ID and password
	fname = os.path.join(home,".netrc")
	if os.path.isfile(fname) and os.access(fname, os.R_OK):
		copyanything(fname,"shared/netrc")

	fname = os.path.join(home,".gitconfig")
	if os.path.isfile(fname) and os.access(fname, os.R_OK):
	    copyanything(fname,"shared/gitconfig")

4) ** Only Required for Cloudubu64dk **
Add the following 2 lines:

	ADD shared/netrc ${HOME}/.netrc
	RUN chown ${USERNAME}:${GROUP} ${HOME}/.netrc

to the file:

	docker-images/jenkins-local/installer/Dockerfile.templ

after the lines:

	#Configure git
	ADD shared/gitconfig ${HOME}/.gitconfig
	RUN chown ${USERNAME}:${GROUP} ${HOME}/.gitconfig

5) As SUDO or ROOT, create the following directories

	mkdir /srv
	mkdir /srv/builds

Then make them readable and writable to the world

	chmod go+rw /srv
	chmod go+rw /srv/builds

6) Configure the docker-images project:

	cd ~/docker-images
	./configure

7) Building the images
```bash

	cd ~/docker-images
	make

Alternately, to capture the output:

	make 2>&1 | tee ../make.log

```
