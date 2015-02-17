REPO_NAME=cloudant/basedev-squeeze

all: build

clean:

build:
	docker build --rm=true -t ${REPO_NAME} .

run:
	docker run --net=host -d ${REPO_NAME}

publish:
	docker push ${REPO_NAME}
