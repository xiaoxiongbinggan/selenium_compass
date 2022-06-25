import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from base.base_page import BasePage
from script.report_data_script import creat_report

from pages.workplace_page.workplace_page import WorkPlace


class Recruit(BasePage):

    url="http://test-cp.youlife.cn/#/workplace/approvalManagement/initiateMine"
    recruit_manage=(By.XPATH,"//*[text()='招聘管理']/..")
    recruit_center=(By.XPATH,"//a[text()='招聘中心']/..")
    # i_need_report=(By.XPATH,"//span[text()='我要报备']/..")
    # i_need_report=(By.XPATH,"//*[@class='anticon anticon-file-text']/..")
    i_need_report_full=(By.XPATH,"/html/body/div[1]/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[3]/button")

    select_input=(By.XPATH,"//div[text()='请选择需求']")
    select_need=(By.XPATH,"//li[@title='测试2022-06-16']")
    next_button=(By.XPATH,"//span[text()='下一步']/..")
    import_demo=(By.XPATH,"//a[text()='《招聘人员报备导入模版》']")
    select_text=(By.XPATH,"//input[@accept='.xlsx, .xls']")
    work_space=(By.XPATH,"//*[text()='工作台']/..")
    tips=(By.XPATH,"//*[@class='ant-message-custom-content ant-message-success']/span")
    clost_btn=(By.XPATH,"//span[@class='ant-modal-close-x']")



    def report(self,number):
        self.click(self.recruit_center)
        print('招聘中心')
        self.click(self.i_need_report_full)
        print('我要报备')
        self.click(self.select_input)
        print('选择需求')
        time.sleep(2)
        self.click(self.select_need)
        print('选择报备测试')
        self.click(self.next_button)
        print("下一步")
        creat_report(number)
        time.sleep(1)
        self.input(self.select_text,r'D:\auto_test\script\报备导入测试数据{0}条.xlsx'.format(number))
        print('上传文件')
        time.sleep(1)
        self.click(self.next_button)
        print("下一步")
        self.assert_text(self.tips,'上传成功！1111')

        print('断言')
        self.click(self.clost_btn)
        print("点击关闭")



if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    s = Service(r"D:\auto_test\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
    print(driver.title)
    driver.implicitly_wait(10)
    wp=WorkPlace(driver)
    wp.open_recruit()
    # time.sleep(1)
    re=Recruit(driver)
    re.report(2)





# select=Select(driver.find_element_by_id('aa'))
# select.select_by_index(1)
# select.select_by_value('')
