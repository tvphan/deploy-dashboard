docker-images
=============

Docker files for development, test and production use. The docker files are grouped into the following categories

* base - Base dockerfiles. Just common and very basic packages.
* jenkins-base - Jenkins basic dockerfiles including SSH + 'jenkins' user configuration.
* base-local - Base development dockerfiles for Cloudant Local.
* jenkins-local - Jenkins specific dockerfiles for Cloudant Local.


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

3) Get the docker-images config file. This is stored in lastpass, under the secure note called "docker-images". Copy and paste the contents of the config file to `~/.docker-images`.

4) Modify the following files under the [shared](shared) folder.

* s3cfg

For each of the files, replace the following values with those from the `~/.docker-images` file.

* Replace **{{aws-access-key-id}}** with the corresponding value from ~/.docker-images.
* Replace **{{aws-secret-access-key}}** with the corresponding value of ~/.docker-images.

Building the images
===================
```bash
cd ~/docker-images
./configure
make
```
