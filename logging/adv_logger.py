import logging

# logger = logging.getLogger("demo_logger")
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# file_handler = logging.FileHandler("demo_logger.log")
# file_handler.setFormatter(formatter)


# class LoggerDemoConsole:
#     def testLog(self):
#         logger = logging.getLogger("test")
#         logger.setLevel(logging.DEBUG)
#
#         consoleHandler = logging.StreamHandler()
#         consoleHandler.setLevel(logging.INFO)
#
#         formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#                                       datefmt="%Y-%m-%d %H:%M:%S")
#
#         consoleHandler.setFormatter(formatter)
#
#         logger.addHandler(consoleHandler)
#
#         logger.debug("test-debug")
#         logger.error("test-error")
#         logger.critical("test-critical")
#         logger.info("test-info")
#
# demo = LoggerDemoConsole()
# demo.testLog()


class FileHandlerLogger:
    def handle_log(self):
        logger = logging.getLogger("file-logger")
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler(filename="file-logger.log",
                                          mode="w")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.info("info")
        logger.error("error")
        logger.critical("critical")

log_handler = FileHandlerLogger()
log_handler.handle_log()


