import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from base.base_page import BasePage
from script.report_data_script import nor_creat_report
from script.report_data_script import abnor_creat_report

from pages.workplace_page.workplace_page import WorkPlace


class Recruit(BasePage):

    url="http://test-cp.youlife.cn/#/workplace/approvalManagement/initiateMine"
    recruit_manage=(By.XPATH,"//*[text()='招聘管理']/..")
    recruit_center=(By.XPATH,"//a[text()='招聘中心']/..")
    i_need_report_full=(By.XPATH,"/html/body/div[1]/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[3]/button")
    abnormal_report_input=(By.XPATH,'//*[text()="异常报备"]/../span')
    select_input=(By.XPATH,"//div[text()='请选择需求']")
    select_need=(By.XPATH,"//li[@title='报备测试']")
    next_button=(By.XPATH,"//span[text()='下一步']/..")
    import_demo=(By.XPATH,"//a[text()='《招聘人员报备导入模版》']")
    select_text=(By.XPATH,"//input[@accept='.xlsx, .xls']")
    work_space=(By.XPATH,"//*[text()='工作台']/..")
    tips=(By.XPATH,"//*[@class='ant-message-custom-content ant-message-success']/span")
    clost_btn=(By.XPATH,"//span[@class='ant-modal-close-x']")

    def normal_report(self,number):
        with allure.step('进入招聘中心'):
            self.click(self.recruit_center)
            time.sleep(1)
        with allure.step('正常报备'):
            self.click(self.i_need_report_full)
            time.sleep(1)
        with allure.step('点击需求框'):
            self.click(self.select_input)
            time.sleep(1)
            self.click(self.select_need)
            self.click(self.next_button)
        with allure.step('生成正常报备数据并上传'):
            nor_creat_report(number)
            time.sleep(1)
            script_path=os.path.abspath(os.path.join(os.getcwd(),'../../../script/'))
            self.input(self.select_text,script_path+'\正常报备测试数据{0}条.xlsx'.format(number))
            time.sleep(2)
            self.click(self.next_button)
            time.sleep(1)
        with allure.step('断言'):
            result=self.assert_text(self.tips,'上传成功！')
            assert result is True
            self.click(self.clost_btn)

    def abnormal_report(self,number):
        with allure.step('进入招聘中心'):
            self.click(self.recruit_center)
            time.sleep(1)
            self.click(self.i_need_report_full)
        with allure.step('选择异常报备'):
            self.click(self.abnormal_report_input)
            time.sleep(1)
            self.click(self.select_input)
            time.sleep(2)
            self.click(self.select_need)
            self.click(self.next_button)
        with allure.step('生成异常报备数据并上传'):
            script_path = os.path.abspath(os.path.join(os.getcwd(), '../../../script/'))
            abnor_creat_report(number)
            time.sleep(1)
            self.input(self.select_text,script_path+'\异常报备测试数据{0}条.xlsx'.format(number))
            time.sleep(2)
            self.click(self.next_button)
        with allure.step('断言'):
            result=self.assert_text(self.tips,'上传成功！')
            assert result is True
            self.click(self.clost_btn)

if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    s = Service(r"D:\selenium_compass\start\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    """
    接管已经打开的指南针界面
    """
    driver.maximize_window()
    print(driver.title)
    driver.implicitly_wait(10)
    wp=WorkPlace(driver)
    wp.open_recruit()
    re=Recruit(driver)
    time.sleep(3)
    re.abnormal_report(10)
    # re.normal_report(10)

    driver.quit()





