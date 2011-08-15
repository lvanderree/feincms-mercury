import os
from django.conf import settings

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = os.path.join(getattr(settings, 'STATIC_URL', ''), 'mercury/javascripts/mercury_loader.js')
    JS_ROOT = os.path.join(getattr(settings, 'STATIC_ROOT', ''), 'mercury/javascripts/')
else:
    pass # not implemented yet

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    CSS_URL = os.path.join(getattr(settings, 'STATIC_URL', ''), 'mercury/stylesheets/structured.css')
else:
    pass # not implemented yet


JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
