import json
from pprint import pprint

import requests
from jsonpath import jsonpath
from requests import Session, Response
from jsonschema import validate
proxies = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888",
}
# 使用模块变量时，建议使用类，避免暴露内容
url_get = "https://httpbin.testing-studio.com/get"


def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)

    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "cccc"
                     })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        params={
            "a": 1,
            "b": 2,
            "c": "cccc"
        },
        data={
            "a": 111,
            "b": 22,
            "c": "cccccccc"
        },
        headers={"h": "header demo"},
        proxies=proxies,
        verify=False
    )
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "header demo"


def test_upload():
    # todo upload fix
    url = "https://httpbin.testing-studio.com/post"
    # url = 'http://httpbin.org/post'
    r = requests.post(
        url,
        files={"file": open("__init__.py", "rb")},
        proxies=proxies,
        verify=False

    )
    print(r.json())
    assert r.status_code == 200


# 构造session机制来追踪用户
def test_session():
    s = Session()
    s.proxies = proxies
    s.verify = False
    s.get(url_get)


# 对response加一些类型，构造一些新的字段，比如解密
def test_hook():
    def modify_response(r, *args, **kwargs):
        # r.content = "OK HOOK SUCCCESS"
        # r.demo = "demo content"
        r.decode_content = "demo content"
        return r

    r = requests.get("https://httpbin.testing-studio.com/get",

                     params={
                         "a": 1,
                         "b": 2,
                         "c": "cccc"
                     },
                     hooks={"response": [modify_response]}
                     )
    print(r.json())
    print(r.demo)
    print(r.decode_content)
    assert r.decode_content == "demo content"
    assert r.status_code == 200


def test_jsonpath():
    r = requests.get("https://home.testing-studio.com/categories.json")
    # print(json.dumps(r.json(), indent=2))
    print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))
    assert r.status_code == 200

    for item in r.json()['category_list']['categories']:
        if item['name'] == '开源项目':
            break
    print(item)
    assert(jsonpath(
        r.json(),
        '$..categories[?(@.name=="开源项目")]'
    )[0]['description']) =='开源项目交流与维护'
    assert item["description"] == '开源项目交流与维护'

# 定义json字段和字段类型
def test_schema():
    r = requests.get("https://home.testing-studio.com/categories.json")
    # print(json.dumps(r.json(), indent=2))
    print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))
    assert r.status_code == 200
    with open("categories.schema.json") as f:
        schema = json.load(f)
    validate(r.json(), schema)
