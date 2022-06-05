from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from selenium.webdriver.chrome.options import Options




class WorkPlace(BasePage):
    url='http://test-cp.tking.com/#/workplace/workplace'
    #页面元素
    approve_manager=(By.XPATH,"//span[text()='审批管理']/..")
    my_approve=(By.XPATH,'//*[@id="popContainer"]/section/aside/div/ul/li[3]/ul/li[2]/a')
    #元素的操作流
    def open_approve(self):
        self.click(self.approve_manager)
        print('审批管理')
        self.click(self.my_approve)
        print('我审批的')


if __name__ == '__main__':
    #接管已经打开的指南针界面
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    chrome_driver = r"D:\auto_test\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    print(driver.title)
    driver.implicitly_wait(10)
    wp=WorkPlace(driver)
    wp.open_approve()

