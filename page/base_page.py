import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.wrapper import handle_black


class BasePage:

    _params = {}


    def __init__(self, driver: WebDriver=None):
        self._driver = driver


    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self,name):
        self._driver.save_screenshot(name)



    def finds(self, locator, value:str=None):
        elements:list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements



    @handle_black
    def find(self, locator, value:str=None):

        element:WebElement

        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element


    @handle_black
    def find_and_text(self, locator, value:str=None):
        element:WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text



    def steps(self, path, name):

        with open(path, encoding='utf-8') as file:
            steps = yaml.safe_load(file)[name]


        raw = json.dumps(steps)
        for key,value in self._params.items():

            # ${name} | name : 12345
            # 12345

            # ${abc} | name : 12345

            raw.replace('${'+ key +'}', value)
        steps = json.loads(raw)


        for step in steps:
            if "action" in step.keys():
                print("多个动作解析")
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                    print("click操作")
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                    print("发送文本")
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0