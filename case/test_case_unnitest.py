from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.workplace_page.workplace_page import WorkPlace
from pages.workplace_page.approve_page.approve_page import Approve
from pages.login_page import Login
import unittest
import yaml

@ddt
class Cases(unittest.TestCase):
    # 测试用例
    @classmethod
    def setUpClass(cls)-> None:#它是一个对函数的类型注解，简单表示方法什么都不返回
        # 接管已经打开的指南针界面
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        # chrome_driver = r"D:\auto_test\chromedriver.exe"
        # cls.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

        # print(cls.driver.title)

        chrome_driver = r"D:\auto_test\chromedriver.exe"
        cls.driver=webdriver.Chrome(chrome_driver)
        cls.driver.implicitly_wait(10)

        #远程启动浏览器
        # cls.driver = webdriver.Remote(command_executor="http://chrome.fyzq.cc/wd/hub",
        #                           desired_capabilities=DesiredCapabilities.CHROME)

        cls.lg = Login(cls.driver)
        cls.driver.get(cls.lg.url)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        cls.wp = WorkPlace(cls.driver)
        cls.ap = Approve(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/approve_memo.yaml')
    def test_01(self, **kwages):
        self.lg.login()

        self.wp.open_approve()
        self.ap.wait_approve(kwages['memo'])



if __name__ == '__main__':
     unittest.main()
