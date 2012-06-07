# From https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spamtests.settings")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# Use twod.wsgi to get webob-compatible requests in Django.
# Downside: it has a hard dependency on old 0.9.x versions of webob.
# http://packages.python.org/twod.wsgi/manual/request-objects.html

from twod.wsgi import DjangoApplication
application = DjangoApplication()

from hamage.middleware import HamageMiddleware
hamage_config = {
    'options': {
        'min_karma': 1,
        'path_configs': [
            {
                # Which paths trigger this handler.
                'path': '/comments/post/',
                # Form field above which to inject error msg.
                'error_field': 'comment',
                # Form field providing author name.
                'author_field': 'name',
             }],
    }
}

application = HamageMiddleware(application, hamage_config)

from wsgiref.simple_server import make_server
port = 8000
server = make_server('', port, application)
print "Serving via wsgiref.simple_server on port %s..." % port
server.serve_forever()


