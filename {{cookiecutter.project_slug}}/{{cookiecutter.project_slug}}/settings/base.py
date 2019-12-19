# SIMPLE SETTINGS STUFF
SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True
}

# REDIS AND CACHE
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

CACHE = {
    'default': {
        'cache': 'aiocache.RedisCache',
        'endpoint': REDIS_HOST,
        'port': int(REDIS_PORT),
        'timeout': 1
    }
}

# TIME CONSTS
SECONDS = 1
MINUTES = SECONDS * 60
HOURS = MINUTES * 60
DAYS = HOURS * 24

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(process)d] [%(levelname)s] %(name)s:%(lineno)d - %(message)s'  # noqa
        },
        'simple': {
            'format': '%(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'asyncio': {
            'level': 'WARNING',
            'propagate': True,
        }
    }
}
