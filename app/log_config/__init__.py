log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['debug_file_handler', 'info_file_handler']},
    'formatters': {
        'info': {
            '()': 'app.log_formatter.RequestFormatter',
            'format': '%(message)s\n'
                      'Log_Level:%(levelname)s Module:%(module)s \n'
                      '[%(time)s]: %(remote_addr)s requested %(url)s\n'
                      'Method:%(request_method)s Duration:%(duration)s\n'
        },
        'debug': {
            '()': 'app.log_formatter.RequestFormatter',
            'format': '%(message)s\n'
                      'Log_Level:%(levelname)s Module:%(module)s \n'
                      '[%(time)s]: %(remote_addr)s requested %(url)s\n'
                      'Method:%(request_method)s Duration:%(duration)s\n'
                      'Host:%(host)s Path:%(request_path)s\n'
        }
    },
    'filters': {
        'show_only_debug': {
            '()': 'app.log_filter.FilterDebug'},
        'show_only_info': {
            '()': 'app.log_filter.FilterInfo'}
    },
    'handlers': {
        'debug_file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'app/logs/debug.log',
            'formatter': 'debug',
            'level': 'DEBUG',
            'filters': ['show_only_debug']
        },
        'info_file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'app/logs/info.log',
            'formatter': 'info',
            'level': 'INFO',
            'filters': ['show_only_info']
        }
    }, }
