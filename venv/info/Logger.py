__author__ = "starry"

from logging import handlers
import logging
import os
class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self,fileName = "./log/server automation.log",when = 'D',level = 'debug',backCount = 3, fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        if not os.path.exists("./log/"):
            os.makedirs("./log/")
        self.logger = logging.getLogger(fileName)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        self.sh = logging.StreamHandler()
        self.sh.setFormatter(format_str)

        self.th =  handlers.TimedRotatingFileHandler(filename = fileName,backupCount = backCount,when = when,encoding='utf-8' )
        self.th.setFormatter(format_str)
        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.th)


# if __name__ == '__main__':
#     log = Logger()
#     log.logger.debug("you is debug")
#     log.logger.info("you is info")
#     log.logger.error("you is error")
#     log.logger.critical("you is critical")
#     log.logger.warning("you is waring")
