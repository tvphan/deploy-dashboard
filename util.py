
import sys

def get_class(name):
    mod, klass = name.rsplit(".", 1)
    __import__(mod)
    mod = sys.modules[mod]
    return getattr(mod, klass, None)

