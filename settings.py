ADMIN = None
FLASK_SETTINGS = { 'DEBUG' : True, 'TESTING' : False}  
DBHOST = None

# Use local_settings.py overrides
import os
fname = os.path.join(os.path.dirname(__file__), "local_settings.py")
execfile(fname)

