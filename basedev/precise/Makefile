REPO_NAME=cloudant/basedev-precise

all: build

clean:

build: 
	docker build --rm=true -t ${REPO_NAME} .

run: 
	docker run -d ${REPO_NAME} 

push:
	docker push ${REPO_NAME}
