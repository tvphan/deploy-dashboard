DIRS= centos6 squeeze precise

all: build

clean:
	for d in $(DIRS); do (cd $$d; $(MAKE) clean); done;

build:
	for d in $(DIRS); do (cd $$d; $(MAKE) build); done;

run:
	for d in $(DIRS); do (cd $$d; $(MAKE) run); done;

push:
	for d in $(DIRS); do (cd $$d; $(MAKE) push); done;
