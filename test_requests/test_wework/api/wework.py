import json
from datetime import datetime

import requests

from test_requests.test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = 'wwd6da61649bd66fea'
    # token可能传多个，不同的应用有不同的token，用dict保存
    token = dict()
    token_time = dict
    secret = "3XBa77sS_W304tGdt-Sc-YManyJ5sKlwq4dSzrIzE_g"

    @classmethod
    def get_token(cls, secret=secret):
        if secret is None:
            # todo:token制度发生变化，在这个地方决定是否重新获取
            return cls.token[secret]
        # secret不在这个词典里面，说明还没出现过，需要赋值，如果已经存在，则直接返回即可。作用：避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            # token跟secret绑定，传什么样的secret就取什么样的token
            cls.token[secret] = r["access_token"]
        # cls.token_time[secret]=datetime.now()
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(
            cls.token_url,
            params={"corpid": cls.corpid, "corpsecret": secret}
        )
        cls.format(r)
        assert r.json()["errcode"] == 0
        return r.json()

