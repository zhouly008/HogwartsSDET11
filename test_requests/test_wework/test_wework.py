import json

import requests


class TestWeWork:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    # corpid = 'ww36536c3b2de54b52'
    corpid = 'wwd6da61649bd66fea'
    # secret = "3SQ3w7I486EJ38UaL6kN-DM3Q1tuWRWqzBg-439S2vU"
    secret = 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
    token=None

    @classmethod
    def setup_class(cls):
        r = requests.get(
            cls.token_url,
            params={"corpid": cls.corpid, "corpsecret": cls.secret}
        )
        assert r.json()["errcode"] == 0

        print(r.json())
        cls.token = r.json()["access_token"]




    def test_get_token(self):
        r=requests.get(
            self.token_url,
            params={"corpid": self.corpid, "corpsecret": self.secret}
            )
        assert r.json()["errcode"]==0

        print(r.json())
        self.token=r.json()["access_token"]

    def test_get_token_exist(self):
        assert self.token is not None

    def test_groupchat_get(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r=requests.post(
            url,
            params={'access_token': self.token},
            json={"offset": 0, "limit": 10}
        )
        print(r.json())

        assert r.json()['errcode']==0

    # 查询群聊的人员信息
    def test_groupchat_detail(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={'access_token': self.token},
            json={"offset": 0, "limit": 10}

        )
        print(r.json())
        assert r.json()['errcode'] == 0

        chat_id=r.json()['group_chat_list'][0]['chat_id']
        detail_url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        r= requests.post(
            detail_url,
            params={'access_token': self.token},
            json={"chat_id": chat_id}
        )
        print(json.dumps(r.json(), indent=2))
        # print(r.json())
        assert r.json()['errcode'] == 0
        assert len(r.json()['group_chat']['member_list']) > 0