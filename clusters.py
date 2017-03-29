
from collections import defaultdict
import json
import os
import time

import httplib2
import settings

# globals for cache
CLUSTERS = None
LAST_UPDATE_TIME = None

# constant
REFRESH_SECS = 0 # number of seconds we refresh CLUSTERS DB

def needs_update():
    if LAST_UPDATE_TIME is None or CLUSTERS is None:
        # not here before, so need an update
        return True
    elif (time.time() - LAST_UPDATE_TIME) > REFRESH_SECS:
        # time is up, refresh
        return True
    else:
        return False


def get_clusters(url):
    global CLUSTERS
    global LAST_UPDATE_TIME

    if needs_update():
        print "check update: ", needs_update()
        c = read_clusters(url)
        # if a non-empty result, update the global variable
        if c:
            LAST_UPDATE_TIME = time.time()
            CLUSTERS = c
        else:
            print "failed to refresh clusters DB, keep previous results"
    return CLUSTERS


# return clusters to the template by querying Clusters DB
def read_clusters(url):
    # return dict of clusters
    h = httplib2.Http()
    h.add_credentials(*settings.ADMIN)
    _, resp = h.request(url)
    #print "resp value: ", resp
    return json.loads(resp)['rows']

