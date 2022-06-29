import inspect


# 打印调用的函数名
import logging


def a():
    print(inspect.stack()[0].function)
    print("a")


def test_stack():
    a()

