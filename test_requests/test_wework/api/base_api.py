import json
import logging

# 基础api，拼装json、params，生成具体的api，拼装请求体，通过send发送
from requests import Request


class BaseApi:
    @classmethod
    def format(cls, r):
        # print(json.dump(r.json(), indent=2))
        # 显示为unicode的内容，而不是编码
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    # todo: 封装类似HttpRunner这样的数据驱动框架
    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            request: Request = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)

    def api_load(self, path):
        pass
