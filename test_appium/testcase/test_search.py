import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page.search("alibaba").get_price("BABA") > 190

    # 参数化，三个参数的名字
    @pytest.mark.parametrize("key, stock_type, price", [
        ("alibaba", "BABA", 190),
        ("JD", "JD", 20)
    ])
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search_page.search(key).get_price(stock_type) > price