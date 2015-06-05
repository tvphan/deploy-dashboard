DIRS = base jenkins-base base-local jenkins-local jenkins-dind

include make/subdirs.mk

jenkins-base: base

jenkins-local: base-local

jenkins-dind: jenkins-base
