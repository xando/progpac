import os
import sys

try:
    virtualenv = os.path.join(os.path.dirname(__file__), ".virtualenv/bin/activate_this.py")
    execfile(virtualenv, dict(__file__=virtualenv))
    sys.path.insert(0, os.path.dirname(__file__))
except IOError:
    pass

os.environ["DJANGO_SETTINGS_MODULE"] = "progpac.settings"
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()