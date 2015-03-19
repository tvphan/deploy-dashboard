DIRS = base base-dev jenkins-dev

include make/subdirs.mk

jenkins-dev: base base-dev
