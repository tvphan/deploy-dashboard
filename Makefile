DIRS = base basedev jenkins

include make/subdirs.mk

jenkins: base basedev
