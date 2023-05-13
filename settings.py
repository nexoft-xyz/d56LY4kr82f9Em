import django_heroku dj_database_url
django_heroku.settings(locals())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
