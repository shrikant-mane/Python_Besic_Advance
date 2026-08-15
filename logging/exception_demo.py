import logging

# logging.basicConfig(filename='myapp.log',
#                     level=logging.DEBUG,
#                     filemode='w',
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%d-%b-%y %H:%M:%S')
#
# """
# % beginning
# asctime ==> dict keys
# ()s  ==> conversion type -- > convert it to string using str()
# """
#
#
# print("logging demo")
#
# logging.info("logging demo")
# logging.warning("logging demo")
# logging.error("logging demo")
# logging.critical("logging demo")
# logging.exception("logging demo")



##########################################
### To handle the logging exception
##########################################

logging.basicConfig(filename="exception.log",
                    level=logging.INFO,
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s)',
                    datefmt='%d-%m-%y %H:%M:%S')

try:
    print(10/0)

except Exception as e:
    logging.error(f"{type(e).__name__}: {e}")
finally:
    print('completed')