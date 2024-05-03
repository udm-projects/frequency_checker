import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

log_formatter = logging.Formatter('%(levelname)s (%(asctime)s) '
                                  '[%(filename)s:%(lineno)s]: %(message)s ')
# ротация файла лога по понедельникам, суммарная длительность - 4 недели
file_handler = TimedRotatingFileHandler(filename='logs/log.log',
                                        encoding='utf-8',
                                        when='W0',
                                        backupCount=3)
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)


console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)