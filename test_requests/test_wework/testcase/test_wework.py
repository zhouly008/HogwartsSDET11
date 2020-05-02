
from test_requests.test_wework.api.wework import WeWork


class TestWeWork:
    # secret = "3XBa77sS_W304tGdt-Sc-YManyJ5sKlwq4dSzrIzE_g"

    @classmethod
    def setup_class(cls):
        # 调用密钥，每个部门都有自己的密钥 #
        cls.token= WeWork.get_token()

    def test_get_token(self):
        # r = requests.get(
        #     self.token_url,
        #     params={"corpid": self.corpid, "corpsecret": self.secret}
        # )
        r = WeWork.get_access_token(WeWork.secret)
        assert r["errcode"] == 0

    def test_get_token_exist(self):
        assert self.token is not None

