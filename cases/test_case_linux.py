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

from pyvirtualdisplay import Display

@pytest.fixture(scope="session")
def linux_driver():
    display = Display(visible= 0, size=(800, 800))
    display.start()
    """
    “–no-sandbox”参数是让Chrome在root权限下跑
    “–headless”参数是不用打开图形界面
    """
    chrome_options=Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    s = Service(r"/opt/chromedriver")
    """ 
    启动浏览器实例
    """
    driver = webdriver.Chrome(service=s, options=chrome_options)
    url = "https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%" \
          "2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoakln867f37kuvrott%26response_type%3D" \
          "code%26scope%3Dsnsapi_login%26state%3DSTATE%26redirect_uri%3Dhttp%253A%252F%252Ftest-cp.youlife.cn%252F%2523%252Flogin"
    driver.get(url)
    lg = Login(driver)
    lg.login()
    driver.maximize_window()
    driver.implicitly_wait(20)

    # 用例执行前置部分
    yield driver
    # 用例执行后置部分
    driver.quit()


@pytest.mark.run(order=1)
@pytest.mark.workspace
@allure.feature("异常报备")
@allure.story("发起异常报备")
@allure.title("发起异常报备")
def test_01(linux_driver):
    wp = WorkPlace(linux_driver)
    re = Recruit(linux_driver)
    wp.open_recruit()
    re.abnormal_report(1)
    time.sleep(1)


@pytest.mark.run(order=2)
@pytest.mark.workspace
@allure.feature("异常报备")
@allure.story("处理异常报备的审批")
@allure.title("处理异常报备的审批")
def test_02(linux_driver):
    wp = WorkPlace(linux_driver)
    ap = Approve(linux_driver)
    wp.open_approve()
    ap.wait_approve()
    time.sleep(1)


@pytest.mark.run(order=3)
@pytest.mark.workspace
@allure.feature("正常报备")
@allure.story("发起正常报备")
@allure.title("发起正常报备")
def test_03(linux_driver):
    wp = WorkPlace(linux_driver)
    re = Recruit(linux_driver)
    wp.open_recruit()
    re.normal_report(3)
    time.sleep(1)


@pytest.mark.run(order=4)
@pytest.mark.workspace
@allure.feature("正常报备")
@allure.story("报备人员面试通过")
@allure.title("报备人员面试通过")
def test_04(linux_driver):
    wp = WorkPlace(linux_driver)
    wp.open_datas()
    dp = DataProcessing(linux_driver)
    dp.interview_results()


if __name__ == '__main__':
    pytest.main()