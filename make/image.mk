all: build

clean::
	$(RM) -r shared

build: Dockerfile
	docker build --rm=true -t ${REPO_NAME} .

run:
	docker run ${DOCKER_RUN_OPTS} -d ${REPO_NAME}

push:
	docker push ${REPO_NAME}

PRJ_DIR = $(abspath ../..)
Dockerfile:
	cd $(PRJ_DIR) && $(PRJ_DIR)/configure
