import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': os.getenv('CACHE_REDIS_HOST', ''),
    'CACHE_REDIS_PORT': os.getenv('CACHE_REDIS_PORT', ''),
    'CACHE_REDIS_DB': os.getenv('CACHE_REDIS_DB', 0),
    'CACHE_REDIS_URL':  os.getenv('CACHE_REDIS_URL', '')}
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SECRET_KEY', '')
