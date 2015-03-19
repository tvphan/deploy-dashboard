DIRS = base jenkins-base base-dev jenkins-dev

include make/subdirs.mk

jenkins-base: base jeknins-base

jenkins-dev: base base-dev
