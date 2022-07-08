from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage

class Login(BasePage):
    url = 'https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoakln867f37kuvrott%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3DSTATE%26redirect_uri%3Dhttp%253A%252F%252Ftest-cp.youlife.cn%252F%2523%252Flogin'
    username=(By.XPATH,"//input[@id='mobile']")
    password=(By.XPATH,"//input[@id='pwd']")
    login_btn=(By.XPATH,"//a[text()='登录并授权']")

    def login(self):

        self.input(self.username,13761362771)
        self.input(self.password,'qinyujie008')
        self.click(self.login_btn)




if __name__ == '__main__':
    chrome_driver = r"D:\selenium_compass\start\chromedriver.exe"
    driver=webdriver.Chrome(chrome_driver)
    lg=Login(driver)
    driver.get(lg.url)
    lg.login()