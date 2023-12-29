"Logging helpers, colors among other things."

import logging
from logging.config import dictConfig

log_fmt = ('\x1b[38;1m[%(asctime)s]\x1b[0m '
           '%(filename)s:%(lineno)d '
           '%(levelcolor)s%(levelname)5.5s '
           '%(name)s%(endcolor)s: '
           '%(message)s')

class ColoringFormatter(logging.Formatter):
    level_color = dict(CRITICAL='31;1',
                       ERROR='31;1',
                       WARNING='33',
                       INFO='32;1',
                       DEBUG='35;1',
                       NOTSET='34;1')

    def __init__(self, format=log_fmt, date_format='%Y-%m-%d %H:%M:%S'):
        logging.Formatter.__init__(self, format, date_format)

    def format(self, record):
        color = self.level_color.get(record.levelname, self.level_color['NOTSET'])
        record.levelcolor = '\x1b[%sm' % (color,)
        record.endcolor = '\x1b[0m'
        return logging.Formatter.format(self, record)


def basic_config(level=logging.INFO, logger=logging.root):
    if [isinstance(h, logging.StreamHandler) and h.stream.isatty() for h in logger.handlers] == [True]:
        [handler] = logger.handlers
    else:
        handler = logging.StreamHandler()
        logger.addHandler(handler)
    formatter = ColoringFormatter()
    handler.setFormatter(formatter)
    logger.setLevel(level)


def default_config():
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'coloring': {
                '()': 'logcolor.ColoringFormatter',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'coloring'
            },
        },
        #'loggers': {'bank': {}},
        'root': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }


def dict_config(cfg):
    dictConfig(cfg)
