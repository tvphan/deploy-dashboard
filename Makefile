DIRS = base jenkins-base base-local jenkins-local

include make/subdirs.mk

jenkins-base: base

jenkins-local: base-local
