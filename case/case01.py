from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_obj.workplace_obj.workplace_page import WorkPlace
from page_obj.workplace_obj.approve_page.approve_page import Approve
import unittest
import yaml

@ddt
class Cases(unittest.TestCase):
    # 测试用例
    @classmethod
    def setUpClass(cls)-> None:#它是一个对函数的类型注解，简单表示方法什么都不返回
        # 接管已经打开的指南针界面
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        chrome_driver = r"D:\auto_test\chromedriver.exe"
        cls.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        cls.driver.implicitly_wait(10)
        print(cls.driver.title)

        cls.wp = WorkPlace(cls.driver)
        cls.ap = Approve(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/approve_memo.yaml')
    def test_01(self, **kwages):
        self.wp.open_approve()
        self.ap.wait_approve(kwages['memo'])



if __name__ == '__main__':
     unittest.main()