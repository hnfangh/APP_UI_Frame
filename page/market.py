from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search import Search


class Market(BasePage):

    def goto_search(self):
        # click
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)