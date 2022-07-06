import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from base.base_page import BasePage
from script.report_data_script import nor_creat_report

from pages.workplace_page.workplace_page import WorkPlace


class DataProcessing(BasePage):
    datas_processing_son=(By.XPATH,"//*[text()='综合数据处理']/../../li")
    fed_back=(By.XPATH,"//*[text()='待反馈']/..")
    choose_checkbox=(By.XPATH,'//div[@class="ant-table-fixed-left"]/div/div/table/tbody/tr[1]/td')
    # selecta=(By.XPATH,'//input[@type="checkbox" and @class="ant-checkbox-input"][1]/..')
    interview_sucess=(By.XPATH,'//*[text()="面试成功"]/..')
    interview_time_select=(By.XPATH,'//*[@placeholder="请选择面试日期"]/..')
    interview_time_now=(By.XPATH,'//*[text()="此刻"]')
    time_confirm_btn=(By.XPATH,'//*[text()="确 定"]/..')
    end_btn=(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[2]')
    def interview_results(self):
        self.click(self.datas_processing_son)
        time.sleep(1)
        print('进入综合数据处理')
        self.click(self.fed_back)
        print('点击待反馈')
        time.sleep(1)
        self.click(self.choose_checkbox)
        print('点击勾选框')
        self.click(self.interview_sucess)
        print('面试成功')
        time.sleep(1)
        self.click(self.interview_time_select)
        print('点击面试时间框')
        time.sleep(1)
        self.click(self.interview_time_now)
        print('选择面试时间')
        self.click(self.time_confirm_btn)
        print('确认')
        time.sleep(1)
        self.click(self.end_btn)
        print('点击结束')




if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    s = Service(r"D:\auto_test\jenkins_selenium_start\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    """
    接管已经打开的指南针界面
    """
    driver.maximize_window()
    print(driver.title)
    driver.implicitly_wait(10)
    wp=WorkPlace(driver)
    wp.open_datas()
    dp=DataProcessing(driver)
    dp.interview_results()