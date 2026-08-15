import logging
import inspect

def getCustomeLogger(level):

    loggername = inspect.stack()[1][3]
    # print("whole: ", inspect.stack())
    # print("[1]: ", inspect.stack()[1])
    # print("[1][0]:", inspect.stack()[1][0])
    # print("[1][1]: ", inspect.stack()[1][1])
    # print("[1][2]:", inspect.stack()[1][2])
    print("[1][3] / loggername: ",loggername)
    logger = logging.getLogger(loggername)
    logger.setLevel(level)


    # fileHandler = logging.FileHandler('custome.log', 'a')
    fileHandler = logging.FileHandler("{}.log".format(loggername), 'w')
    fileHandler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger