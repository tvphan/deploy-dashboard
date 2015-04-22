REPO_NAME=cloudant/jenkins-local-installer
include ../../make/image.mk

clean::
	$(RM) Dockerfile

run:
	docker run --mac-address="02:d0:c6:0a:29:33" -d ${REPO_NAME}
