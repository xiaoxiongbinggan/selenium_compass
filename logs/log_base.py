import logging

import allure

def logger_console():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    console=logging.StreamHandler()
    #创建控制台

    logger.addHandler(console)
    #日志信息输出到控制台

    fmt='%(asctime)s%(filename)s%(levelname)s%(message)s'
    fomator=logging.Formatter(fmt)
    #创建格式器 ：日志生成时间 日志文件名。。。

    console.setFormatter(fomator)
    #格式器输出给控制台

    return logger

def logger_text():
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    filehandle=logging.FileHandler('../logs/mylog.log',encoding='utf-8')
    #创建文本处理器 指定信息输出到文本处理器

    logger.addHandler(filehandle)
    #日志信息输入到文本处理器

    fmt='%(asctime)s%(filename)s%(levelname)s%(message)s'
    fomator=logging.Formatter(fmt)
    #创建格式器 ：日志生成时间 日志文件名。。。

    filehandle.setFormatter(fomator)
    #格式器输出给文本处理器

    # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s%(filename)s%(levelname)s%(message)s',datefmt='%a%d%b%Y%H:%M%S',filename='./logs/mylog.log',filemode='a')
    return logger