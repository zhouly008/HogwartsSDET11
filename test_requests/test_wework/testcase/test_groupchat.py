from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWeWork:
    @classmethod
    def setup_class(cls):
        cls.groupchat = GroupChat()
        # 调用密钥，每个部门都有自己的密钥,# 在case的内部的groupchat搞定了token的获取
        # cls.token = WeWork.get_token(cls.groupchat.secret)

    # 把稳定的具有业务含义的功能封装到细节里,入参决定要测试的数据，返回值决定要断言的数据，case是
    # 稳定的，po是封装的思想
    def test_groupchat_get(self):
        r = self.groupchat.list()
        assert r['errcode'] == 0

    def test_groupchat_get_status(self):
        r = self.groupchat.list(offset=0, limit=10, status_filter=1)
        assert r["errcode"] == 0

    # 查询群聊的人员信息,直接返回json
    def test_groupchat_detail(self):
        r = self.groupchat.list(offset=0, limit=10, )
        assert r['errcode'] == 0

        chat_id = r['group_chat_list'][0]['chat_id']
        r = self.groupchat.get(chat_id)

        # print(r.json())
        assert r['errcode'] == 0
        assert len(r['group_chat']['member_list']) > 0
