import requests

from test_requests.test_wework.api.wework import WeWork


class Tag(WeWork):
    def get(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?"
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json={"tag_id": []}
        )
        # 打印一下输出，返回json
        self.format(r)
        return r.json()

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
         pass

