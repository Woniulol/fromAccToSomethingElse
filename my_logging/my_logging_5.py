import logging
import logging.config


logging.config.fileConfig("logging.conf")
# logging.config.dictConfig()

rootLogger = logging.getLogger()
rootLogger.debug("This is a root logger")

logger = logging.getLogger("applog")
logger.debug("this is applog, debug")

try:
    a = "abc"
    int(a)
except Exception as e:
    logger.error(e)  # error message 并不完整
    logger.exception(e)  # error message 完整
