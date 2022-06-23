import allure
import pytest
from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from page_obj.workplace_obj.workplace_page import WorkPlace
from page_obj.workplace_obj.approve_page.approve_page import Approve
from page_obj.login_page import Login
from page_obj.workplace_obj.recruit_page.recruit_page import Recruit
import unittest
import yaml


# 测试用例
@pytest.fixture(scope="session")
def driver():

    #远程启动浏览器
    #driver = webdriver.Remote(command_executor="http://chrome.fyzq.cc/wd/hub",
    #                           desired_capabilities=DesiredCapabilities.CHROME)

    # 接管已经打开的浏览器
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    # chrome_driver = r"D:\auto_test\chromedriver.exe"
    # cls.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    # print(cls.driver.title)

    chrome_driver = r"D:\auto_test\chromedriver.exe"
    driver=webdriver.Chrome(chrome_driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    lg = Login(driver)
    driver.get(lg.url)

    #用例执行前置部分
    yield driver
    #用例执行后置部分
    driver.quit()




@pytest.fixture(scope="session")
def user_driver():
    s=Service(r"D:\auto_test\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=Options())
    driver.get("https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoakln867f37kuvrott%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3DSTATE%26redirect_uri%3Dhttp%253A%252F%252Ftest-cp.youlife.cn%252F%2523%252Flogin")
    lg=Login(driver)
    lg.login()
    driver.maximize_window()
    driver.implicitly_wait(20)


    #用例执行前置部分
    yield driver
    #用例执行后置部分
    driver.quit()

@allure.title("测试登录-审批管理")
# @pytest.mark.parametrize("memo",['测试备注1','测试备注2'])
def test_01(user_driver):
    wp = WorkPlace(user_driver)
    ap = Approve(user_driver)
    wp.open_approve()
    ap.wait_approve()

@allure.title("测试登录-我要报备")
def test_02(user_driver):

    wp=WorkPlace(user_driver)
    re=Recruit(user_driver)
    wp.open_recruit()
    re.report(3)






if __name__ == '__main__':
 pytest.main()