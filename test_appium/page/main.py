from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.search import Search


class Main(BasePage):

    @property
    def goto_search_page(self):
        #  self._driver.find_element(MobileBy.ID, "tv_search").click()
        self.find(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    def goto_stocks(self):
        pass

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass

    def goto_messages(self):
        pass
