import logging

# DEBUG 10
# INFO 20
# WARNING 30
# ERROR 40
# CRITICAL 50

# only level about the info will be output
# use baseConfig() to reset the level, log to a file, set writing mode
logging.basicConfig(level=logging.INFO, filename="demo.log", filemode="w")

name = "aaa"
age = 18

logging.debug("this is debug log")
logging.info(f"the name is {name}, age is {age}")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")

# INFO:root:the name is aaa, age is 18
# WARNING:root:this is warning log
# ERROR:root:this is error log
# CRITICAL:root:this is critical log

# you have the level, root and the log
