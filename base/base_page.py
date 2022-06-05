from time import sleep

from selenium import webdriver


class BasePage:
    # driver=webdriver.Chrome()
    # 初始化浏览器

    #构造函数：调用类对象的时候需要调用的函数
    def __init__(self, driver):
        self.driver = driver

    # 访问URL
    def visit(self, url):
        self.driver.get(url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()

    def assert_text(self,loc,expect):
        try:
            assert expect in self.locator(loc).text
        except:
            return False


    def quit(self):
        self.driver.quit()
