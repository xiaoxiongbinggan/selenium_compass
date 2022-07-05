import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pages.workplace_page.workplace_page import WorkPlace
class Approve(BasePage):
    url='http://test-cp.tking.com/#/workplace/approvalManagement/approvalMine'
    my_approve = (By.XPATH, '//*[@id="popContainer"]/section/aside/div/ul/li[3]/ul/li[2]/a')
    type=(By.XPATH,"//span[text()='工资付款 ']/..")
    type2=(By.XPATH,"//span[text()='异常报备 ']/..")
    detail=(By.XPATH,'//*[@class="ant-table-fixed-right"]/div/div/table/tbody/tr[1]/td')
    approve_memo=(By.XPATH,'//input[@placeholder="请输入审批意见"]')

    pass_btn=(By.XPATH,"//span[text()='通 过']/..")
    confirm_btn=(By.XPATH,'//span[text()="确 定"]/..')
    tips=(By.XPATH,'//div[@class="ant-message"]')
    close_btn=(By.XPATH,'//button[@class="ant-drawer-close"]')

    def wait_approve(self):
        self.click(self.my_approve)
        print('我审批的')
        self.click(self.type)
        print('选择审批类型')
        time.sleep(3)
        self.click(self.detail)
        # time.sleep(3)
        print('打开详情')
        time.sleep(1)
        # self.input(self.approve_memo,time.localtime())


        # print('输入审批备注')
        # self.click(self.pass_btn2)
        # print('通过')
        # self.click(self.confirm_btn)
        # print('确认')

        self.click(self.close_btn)
        print('关闭')


if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    s = Service(r"D:\auto_test\jenkins_selenium_start\chromedriver.exe")
    driver = webdriver.Chrome( service=s, options=chrome_options)
    """
    接管已经打开的指南针界面
    """
    print(driver.title)
    driver.implicitly_wait(10)
    wp=WorkPlace(driver)
    wp.open_approve()

    ap=Approve(driver)
    # memo='测试备注'
    ap.wait_approve()