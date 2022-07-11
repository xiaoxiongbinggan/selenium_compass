import logging
import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from logs import log_base

logger=log_base.logger_console()
logger2=log_base.logger_text()
class BasePage:


    #构造函数：只要调用类对象就会执行的函数，其他函数需要调用对应函数才会执行该函数
    def __init__(self, driver):
        self.driver = driver



    def locator(self, loc):
        logging.info('定位元素{}'.format(loc))
        time.sleep(0.3)
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            self.screen_short()
        finally:
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

    def screen_short(self):
        file_path=r'D:\selenium_compass\files\screenshots'
        file_name=time.strftime("%Y%m%d-%H%M%S")+'.png'
        filename =os.path.join(file_path,file_name)
        self.driver.get_screenshot_as_file(filename)
        print(filename)

    def quit(self):
        logging.info('退出浏览器')
        self.driver.quit()
