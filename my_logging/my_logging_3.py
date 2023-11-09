import logging

# DEBUG 10
# INFO 20
# WARNING 30
# ERROR 40
# CRITICAL 50

# only level about the info will be output
# use baseConfig() to reset the level, log to a file, set writing mode
logging.basicConfig(
    level=logging.INFO,
    filename="demo.log",
    filemode="w",
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s | %(levelname)s | %(filename)s : %(lineno)s | %(message)s",
)

name = "aaa"
age = 18

logging.info(f"the name is {name}, the age is {age}.")

logging.warning(f"the name is {name}, the age is {age}.")

# 2023-11-09 22:12:45 | INFO | my_logging_3.py : 22 | the name is aaa, the age is 18.
# 2023-11-09 22:12:45 | WARNING | my_logging_3.py : 24 | the name is aaa, the age is 18.
