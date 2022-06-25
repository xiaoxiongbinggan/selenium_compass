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
    # type2=(By.XPATH,"//span[text()='发薪申请 ']/..")
    type3=(By.XPATH,"//span[text()='工资付款 ']/../../label[3]")
    # type1=(By.XPATH,'//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/label[1]/span[2]')
    detail=(By.XPATH,'//div[@class="ant-table-fixed-right"]/div/div/table/tbody/tr[1]/td/a')
    pass_btn=(By.XPATH,"//span[text()='通 过']/..")
    pass_btn2=(By.LINK_TEXT,"通 过")
    pass_memo=(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/span/input')
    confirm_btn=(By.XPATH,'//span[text()="确 定"]/..')
    tips=(By.XPATH,'//div[@class="ant-message"]')
    close_btn=(By.XPATH,'//button[@class="ant-drawer-close"]')

    def wait_approve(self):
        self.click(self.my_approve)
        print('我审批的')
        self.click(self.type3)
        print('选择审批类型')
        time.sleep(3)
        self.click(self.detail)
        # time.sleep(3)
        print('打开详情')
        self.click(self.close_btn)
        print('关闭')
        # self.input(self.pass_memo,time.ctime())
        # self.input(self.pass_memo,memo)
        # print('输入审批备注')
        # self.click(self.pass_btn2)
        # print('通过')
        # self.click(self.confirm_btn)
        # print('确认')
        # # self.assert_text(self.tips,'提示-该问款单号问款信息不存在,问款单号：KFWK20220517000001')



if __name__ == '__main__':
    #接管已经打开的指南针界面


    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    s=Service( r"D:\auto_test\chromedriver.exe")
    driver = webdriver.Chrome( service=s, options=chrome_options)
    print(driver.title)
    driver.implicitly_wait(10)
    wp=WorkPlace(driver)
    wp.open_approve()

    ap=Approve(driver)
    # memo='测试备注'
    ap.wait_approve()