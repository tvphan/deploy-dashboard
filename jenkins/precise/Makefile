REPO_NAME=cloudant/jenkins-precise

all: build

clean:
	rm -rf shared

build:
	docker build --rm=true -t ${REPO_NAME} .

run:
	docker run --net=host -d ${REPO_NAME}

push:
	docker push ${REPO_NAME}
