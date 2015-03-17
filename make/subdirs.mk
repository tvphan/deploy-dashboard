CLEANDIRS = $(DIRS:%=clean-%)
BUILDDIRS = $(DIRS:%=build-%)
RUNDIRS   = $(DIRS:%=run-%)
PUSHDIRS  = $(DIRS:%=push-%)

all: $(BUILDDIRS)
$(DIRS): $(BUILDDIRS)
$(BUILDDIRS):
	$(MAKE) -C $(@:build-%=%)

clean: $(CLEANDIRS)
$(CLEANDIRS):
	$(MAKE) -C $(@:clean-%=%) clean

run: $(RUNDIRS)
$(RUNDIRS):
	$(MAKE) -C $(@:run-%=%) run

push: $(PUSHDIRS)
$(PUSHDIRS):
	$(MAKE) -C $(@:push-%=%) push

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(CLEANDIRS)
.PHONY: subdirs $(BUILDDIRS)
.PHONY: subdirs $(RUNDIRS)
.PHONY: subdirs $(PUSHDIRS)
.PHONY: all clean run push
