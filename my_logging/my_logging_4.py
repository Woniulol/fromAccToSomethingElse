import logging

# Loggers
# 提供程序能够使用的接口
# 笔

logger = logging.getLogger()
print(logger)
# <RootLogger root (WARNING)>
# 是一个RootLogger 名字叫root 默认级别是WARNING
print(type(logger))
# <class 'logging.RootLogger'>
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 给logger设置一个最低的级别，当Handler的级别更高的时候就会优先使用每一个Handler的级别
# 如果logger的级别更高，那么Handler并不会覆盖logger本身的级别
print(logger)
# <Logger __main__ (INFO)>

# Handlers
# 将记录器生成的日记发送到目的地
# 笔往哪里写
# 常用的handler
# StreamHandler, FileHandler, BaseRotatingHandler, QueueHandler TimedRotatingFileHandler...
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename="addDemo.log", mode="w")
fileHandler.setLevel(logging.INFO)
# 不像consoleHandler，fileHandler没有被指定具体的输出级别
# level会直接跟随logger的输出级别

# Formatters
# 设置日志内容组成的结构和消息字段
# 写出来什么东西
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)8s | %(filename)s : %(lineno)s | %(message)s"
)
# 8s: 让所有的levelname占8位

# 把上面三个连起来
# 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
# 给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# Filters
# 决定哪些日志会被输出
# 往哪里写的级别
flt = logging.Filter("aaa")
# 以cn.cccb开头的logger name
# 是logger的名字，不是log的具体内容
# logger.addFilter(filter=flt)

consoleHandler.addFilter(filter=flt)
# file里面有，控制台没有


# 打印日志代码
logger.debug("this is debug log")
logger.info("this is info log")
logger.warning("this is warning log")
logger.error("this is error log")
logger.critical("this is critical log")
