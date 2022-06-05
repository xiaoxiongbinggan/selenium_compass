import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from base.base_page import BasePage
class Approve(BasePage):
    url='http://test-cp.tking.com/#/workplace/approvalManagement/approvalMine'
    type2=(By.XPATH,"//span[text()='发薪申请 ']/..")
    type3=(By.XPATH,"//span[text()='工资付款 ']/..")
    type1=(By.XPATH,'//*[@id="popContainer"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/label[1]/span[2]')
    type4=(By.XPATH,"")
    detail=(By.XPATH,'//td[@class="ant-table-row-cell-break-word"]')
    pass_btn=(By.XPATH,"//span[text()='通 过']/..")
    pass_btn2=(By.LINK_TEXT,"通 过")
    pass_memo=(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/span/input')
    confirm_btn=(By.XPATH,'//span[text()="确 定"]/..')
    tips=(By.XPATH,'//div[@class="ant-message"]')

    def wait_approve(self,memo):
        self.click(self.type3)
        print('审批类型2')
        time.sleep(3)
        self.click(self.detail)
        time.sleep(3)
        print('打开详情')
        # self.input(self.pass_memo,time.ctime())
        self.input(self.pass_memo,memo)
        print('输入审批备注')
        self.click(self.pass_btn2)
        print('通过')
        self.click(self.confirm_btn)
        print('确认')
        # self.assert_text(self.tips,'提示-该问款单号问款信息不存在,问款单号：KFWK20220517000001')



    def approve_passed(self):
        self.click(self.type1)
        print('审批通过')
        self.click(self.type2)
        print('详情')

if __name__ == '__main__':
    #接管已经打开的指南针界面
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    chrome_driver = r"D:\auto_test\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    print(driver.title)
    driver.implicitly_wait(10)
    ap=Approve(driver)
    memo='测试备注'
    ap.wait_approve(memo)