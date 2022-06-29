import inspect

import yaml


def test_yaml_load():
    with open('../page/main.yaml', encoding='utf-8') as file:
        name = inspect.stack()[1].fuction
        steps = yaml.safe_load(file)[name]
    for step in steps:
        if "by" in steps.keys():
            print("查找元素")
        if "action" in steps.keys():
            print("多个动作解析")
            action = step["action"]
            if "click" == action:
                print("click操作")
            if "send" == action:
                value = step["value"]
                print(f"send{value}")

# 替换原理
def test_replace():
    _prames={"name":"1234"}
    str = "xxxxxxxxxx${name}xxxxxxxxxxx"
    for key,value in _prames.items():
        str = str.replace(f"${{{key}}}", value)
    print(str)