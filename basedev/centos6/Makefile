REPO_NAME=cloudant/basedev-centos6

all: build

clean:

build: 
	docker build --rm=true -t ${REPO_NAME} .

run: 
	docker run -d ${REPO_NAME} 

publish:
	docker push ${REPO_NAME}
