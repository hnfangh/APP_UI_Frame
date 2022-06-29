from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    def start(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = ".view.WelcomeActivityAlias"
            desired_caps['noReset'] = True
            desired_caps['noSign'] = True
            desired_caps['newCommandTimeout'] = 10000
            # 初始化driver
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)
        # 返回自身，对另一个方法定义
        return self

    def stop(self):
        pass


    def restart(self):
        pass


    def main(self) -> Main: # 指定返回类型

        # 把driver传给main，否则默认为None
        return Main(self._driver)



