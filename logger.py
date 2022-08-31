logger_config = {
    'version': 1,
    'formatters': {
        'formatting_errors': {'format': '{asctime} - {funcName} -'
                                        ' {lineno} - {message}',
                              'style': '{'},
        'formatting_info': {'format': '{asctime} - {message}',
                            'style': '{'}
        },

    'handlers': {
        'error': {
            'class': 'logging.FileHandler',
            'filename': '/root/botTVin/loggins/error.log',
            'mode': 'a',
            'level': 'ERROR',
            'formatter': 'formatting_errors'
            },
        'info': {
            'class': 'logging.FileHandler',
            'filename': '/root/botTVin/loggins/info.log',
            'mode': 'a',
            'level': 'INFO',
            'formatter': 'formatting_info'
            }
        },


    'loggers': {
        'app_error': {
            'level': 'ERROR',
            'handlers': ['error'],
            'propagate': False
            },
        'app_info': {
            'level': 'INFO',
            'handlers': ['info'],
            'propagate': False
        }
    },


    'disable_existing_loggers': False,
    'filters': {},
}