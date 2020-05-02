from test_requests.test_wework.api.tag import Tag


class TestTag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    def test_get(self):
        r = self.tag.get()
        assert r['errcode'] == 0
