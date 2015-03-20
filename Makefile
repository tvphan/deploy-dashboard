DIRS = base jenkins-base base-local jenkins-local

include make/subdirs.mk

jenkins-base: base jenkins-base

jenkins-local: base base-local
