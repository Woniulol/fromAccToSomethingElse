import logging

# DEBUG 10
# INFO 20
# WARNING 30
# ERROR 40
# CRITICAL 50

# only level about the info will be output
# use baseConfig() to reset the level, log to a file, set writing mode
logging.basicConfig(level=logging.DEBUG, filename="demo.log", filemode="w")

logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")
