import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login
from pages.workplace_page.approve_page.approve_page import Approve
from pages.workplace_page.data_processing_page.data_processing_page import DataProcessing
from pages.workplace_page.recruit_page.recruit_page import Recruit
from pages.workplace_page.workplace_page import WorkPlace


# 测试用例
@pytest.fixture(scope="session")
def windows_remote_driver():
    """远程启动redmi电脑的浏览器"""
    # driver = webdriver.Remote(command_executor="http://chrome.fyzq.cc/wd/hub",
    #                           desired_capabilities=DesiredCapabilities.CHROME)


    """ 远程启动浏览器配置1"""
    desired_caps={}
    desired_caps['platform'] = 'WINDOWS'
    desired_caps['browserName'] = 'chrome'
    driver = webdriver.Remote('http://192.168.7.10:4444/wd/hub',desired_caps)

    """ 远程启动浏览器配置2"""
    # driver = webdriver.Remote( command_executor='http://192.168.7.10:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)

    url="https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%" \
        "2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoakln867f37kuvrott%26response_type%3D" \
        "code%26scope%3Dsnsapi_login%26state%3DSTATE%26redirect_uri%3Dhttp%253A%252F%252Ftest-cp.youlife.cn%252F%2523%252Flogin"
    driver.get(url)
    lg=Login(driver)
    lg.login()
    driver.maximize_window()
    driver.implicitly_wait(20)

    #用例执行前置部分
    yield driver
    #用例执行后置部分
    driver.quit()

@pytest.fixture(scope="session")
def user_driver():
    s=Service(r"D:\selenium_compass\start\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=Options())
    url="https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%" \
        "2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoakln867f37kuvrott%26response_type%3D" \
        "code%26scope%3Dsnsapi_login%26state%3DSTATE%26redirect_uri%3Dhttp%253A%252F%252Ftest-cp.youlife.cn%252F%2523%252Flogin"

    driver.get(url)
    lg=Login(driver)
    lg.login()
    driver.maximize_window()
    driver.implicitly_wait(20)

    #用例执行前置部分
    yield driver
    #用例执行后置部分
    driver.quit()



@pytest.mark.run(order=1)
@pytest.mark.workspace
@allure.feature("异常报备")
@allure.story("发起异常报备")
@allure.title("发起异常报备")
def test_01(user_driver):
    wp=WorkPlace(user_driver)
    re = Recruit(user_driver)
    wp.open_recruit()
    re.abnormal_report(1)
    time.sleep(1)


@pytest.mark.run(order=2)
@pytest.mark.workspace
@allure.feature("异常报备")
@allure.story("处理异常报备的审批")
@allure.title("处理异常报备的审批")

def test_02(windows_remote_driver):
    wp = WorkPlace(windows_remote_driver)
    ap = Approve(windows_remote_driver)
    wp.open_approve()
    ap.wait_approve()
    time.sleep(1)

@pytest.mark.run(order=3)
@pytest.mark.workspace
@allure.feature("正常报备")
@allure.story("发起正常报备")
@allure.title("发起正常报备")
def test_03(windows_remote_driver):
    wp=WorkPlace(windows_remote_driver)
    re=Recruit(windows_remote_driver)
    wp.open_recruit()
    re.normal_report(3)
    time.sleep(1)

@pytest.mark.run(order=4)
@pytest.mark.workspace
@allure.feature("正常报备")
@allure.story("报备人员面试通过")
@allure.title("报备人员面试通过")
def test_04(windows_remote_driver):
    wp = WorkPlace(windows_remote_driver)
    wp.open_datas()
    dp=DataProcessing(windows_remote_driver)
    dp.interview_results()






if __name__ == '__main__':
 pytest.main()
