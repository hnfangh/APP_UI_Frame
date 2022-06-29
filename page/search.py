
from page.base_page import BasePage


class Search(BasePage):

    def search(self, name):
        self._driver.save_screenshot("search.png")
        self._params["name"] = name
        self.steps("../page/search.yaml")

    def is_choose(self, name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")

    def reset(self, name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")

    def add(self, name):
        self._driver.save_screenshot("add.png")
        self._params["name"] = name
        self.steps("../page/search.yaml")

