import logging
import logging.config

class LoggerDemoConf():
    def test_log(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)
        print(logger)
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')

log = LoggerDemoConf()
log.test_log()


