"""
WSGI config for project.

WARNING
THIS WSGI does not work with django runserver

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
import site

ALLDIRS = ['/home/msjohans/PehmoGIS/geon_new/lib/python2.6/site-packages']

# Remember original sys.path.
prev_sys_path = list(sys.path)

# Add each new site-packages directory.
for directory in ALLDIRS:
    site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['PYTHON_EGG_CACHE'] = '/home/msjohans/PehmoGIS/Questionnaire-prototype/quest_proto/egg_cache'

sys.path.append('/home/msjohans/PehmoGIS/Questionnaire-prototype/quest_proto')
sys.path.append('/home/msjohans/PehmoGIS/Questionnaire-prototype/quest_proto/quest_proto')

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quest_proto.settings")

#import quest_proto.settings as loaded_settings
#loaded_settings.SITE_ID = 20 # This should come from the database

#config = {}
#for setting in dir(loaded_settings):
#    if setting == setting.upper():
#        config[setting] = getattr(loaded_settings, setting)
#    
#
#from django.conf import settings
#print (settings.FORCE_SCRIPT_NAME)
#print(loaded_settings.SITE_ID)
#settings.configure(**config)
#print(settings.SITE_ID)



# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

def application(environ, start_response):
    import psycopg2
    if environ.get('HTTP_HOST'):
        host = environ['HTTP_HOST']
    else:
        host = environ['SERVER_NAME']
    import quest_proto.settings as loaded_settings
    dbname = loaded_settings.DATABASES['default']['NAME']
    dbuser = loaded_settings.DATABASES['default']['USER']
    dbpasswd = loaded_settings.DATABASES['default']['PASSWORD']
    dbhost = loaded_settings.DATABASES['default']['HOST']
    dbport = loaded_settings.DATABASES['default']['PORT']
    conn = psycopg2.connect(database=dbname,user=dbuser,password=dbpasswd,host=dbhost,port=dbport);
    cur = conn.cursor()
    cur.execute("SELECT ID FROM django_site WHERE domain like %s;", ("%" + host,))
    site_id = cur.fetchone()
    cur.close()
    conn.close()
    
    loaded_settings.SITE_ID = site_id[0]
    if loaded_settings.SITE_ID == None:
        loaded_settings.SITE_ID = 1

    config = {}
    for setting in dir(loaded_settings):
        if setting == setting.upper():
            config[setting] = getattr(loaded_settings, setting)

    from django.conf import settings
    if not settings.configured:
        settings.configure(**config)

#    from django.core.wsgi import get_wsgi_application
#    _application = get_wsgi_application()
    return _application(environ, start_response)

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
