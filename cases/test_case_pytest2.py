import allure
import pytest
from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from base.base_page import BasePage
from pages.workplace_page.workplace_page import WorkPlace
from pages.workplace_page.approve_page.approve_page import Approve
from pages.login_page import Login
from pages.workplace_page.recruit_page.recruit_page import Recruit
import yaml
from logs import log_base
class TestCase(BasePage):

    #远程启动浏览器
    #driver = webdriver.Remote(command_executor="http://chrome.fyzq.cc/wd/hub",
    #                           desired_capabilities=DesiredCapabilities.CHROME)

    # 接管已经打开的浏览器
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    # chrome_driver = r"D:\auto_test\chromedriver.exe"
    # cls.driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    # print(cls.driver.title)


    # @pytest.fixture(scope="session")
    def setUp_Class(self):
        login_url = "https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoakln867f37kuvrott%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3DSTATE%26redirect_uri%3Dhttp%253A%252F%252Ftest-cp.youlife.cn%252F%2523%252Flogin"
        s = Service(r"D:\auto_test\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s, options=Options())
        driver.get(login_url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        lg = Login(driver)
        lg.login()

    def tearDown_Class(self):
        self.driver.quit()

    @allure.title("测试登录-审批管理")
    # @pytest.mark.parametrize("memo",['测试备注1','测试备注2'])
    def test_01(self):
        wp = WorkPlace(self.driver)
        ap = Approve(self.driver)
        wp.open_approve()
        ap.wait_approve()

    @allure.title("测试登录-我要报备")
    def test_02(self):
        wp=WorkPlace(self.driver)
        re=Recruit(self.driver)
        wp.open_recruit()
        re.report(3)



if __name__ == '__main__':
    pytest.main()