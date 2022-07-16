import os
import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from base.base_page import BasePage

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
    @allure.step("step:步骤")
    def interview_results(self):
        allure.dynamic.description('描述：')
        with allure.step('进入综合数据处理'):
            self.click(self.datas_processing_son)
            time.sleep(1)
        with allure.step('点击待反馈'):
            self.click(self.fed_back)
            time.sleep(1)
        with allure.step('点击勾选框'):
            self.click(self.choose_checkbox)
        with allure.step('面试成功'):
            self.click(self.interview_sucess)
            time.sleep(1)
        with allure.step('点击面试时间框'):
            self.click(self.interview_time_select)
            time.sleep(1)
        with allure.step('选择面试时间'):
            self.click(self.interview_time_now)
        with allure.step('确认'):
            self.click(self.time_confirm_btn)
            time.sleep(1)
            screen_short=self.driver.get_screenshot_as_png()
            allure.attach(screen_short)
        with allure.step('点击结束'):
            self.click(self.end_btn)




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
    wp.open_datas()
    dp=DataProcessing(driver)
    dp.interview_results()
    driver.quit()
