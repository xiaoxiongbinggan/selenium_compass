import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from base.base_page import BasePage
from selenium.webdriver.chrome.options import Options



class WorkPlace(BasePage):
    url='http://test-cp.tking.com/#/workplace/workplace'
    #页面元素
    approve_manage=(By.XPATH,"//span[text()='审批管理']/..")

    recruit_manage=(By.XPATH,"//span[text()='招聘管理']/..")
    recruit_center = (By.XPATH, "//div[@aria-owns='/workplace/recruitmentCenter$Menu']")
    data_center=(By.XPATH,"//*[text()='综合数据处理']/../../../li[2]/div[1]")

    #元素的操作流
    def open_approve(self):
        allure.dynamic.description('审批管理')
        self.click(self.approve_manage)

    def open_recruit(self):
        allure.dynamic.description('招聘管理')
        self.click(self.recruit_manage)


    def open_datas(self):
        allure.dynamic.description('综合数据处理')
        self.click(self.data_center)









if __name__ == '__main__':
    #接管已经打开的指南针界面
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
    wp = WorkPlace(driver)
    wp.open_recruit()
    time.sleep(1)
    driver.quit()


