import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from logs import log_base

logger=log_base.logger_console()

class BasePage:
    # driver=webdriver.Chrome()
    # 初始化浏览器

    #构造函数：调用类对象的时候需要调用的函数
    def __init__(self, driver):
        self.driver = driver


    def locator(self, loc):
        logging.info('定位元素{}'.format(loc))
        return self.driver.find_element(*loc)


    def input(self, loc, txt):
        logging.info('{}输入框输入{}'.format(loc,txt))
        self.locator(loc).send_keys(txt)

    def click(self, loc):
            logging.info('点击元素{}'.format(loc))
            self.locator(loc).click()


    def assert_text(self,loc,expect):
        logging.info('断言有无{}'.format(expect))
        try:
            assert expect in self.locator(loc).text
        except:
            return False


    def quit(self):
        logging.info('退出浏览器')
        self.driver.quit()
