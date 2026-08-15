import logging
from customelogger import getCustomeLogger

class LoggingDemo:

    def m1(self):
        logger = getCustomeLogger(logging.DEBUG)
        logger.debug('m1: debug')
        logger.info('m1: info')
        logger.warning('m1: warning')
        logger.error('m1: error')
        logger.critical('m1: critical')

    def m2(self):
        logger = getCustomeLogger(logging.WARNING)
        logger.debug('m2: debug')
        logger.info('m2: info')
        logger.warning('m2: warning')
        logger.error('m2: error')
        logger.critical('m2: critical')

    def m3(self):
        logger = getCustomeLogger(logging.ERROR)
        logger.debug('m3: debug')
        logger.info('m3: info')
        logger.warning('m3: warning')
        logger.error('m3: error')
        logger.critical('m3: critical')

l = LoggingDemo()
l.m1()
l.m2()
l.m3()