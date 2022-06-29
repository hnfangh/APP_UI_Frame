
# 装饰器学习


'''
    装饰器第一部分before
'''

def tmp():
    print("hello")
    print("tmp")
    print("world")



def tmp1():
    print("hello")
    print("tmp1")
    print("world")



def test_wrapper():
    tmp()
    tmp1()



'''
    装饰器第二部分 公共方法抽离
'''

def extend(func):
    def hello(*args,**kwargs):
        print("hello")
        func(*args,**kwargs)
        print("world")
    return hello



@extend
def tmp():
    print("tmp")

@extend
def tmp1():
    print("tmp1")



def test_wrapper_one():
    tmp()
    tmp1()



'''
    装饰器第三部分 带参数
'''


def extend(func):
    def hello(*args,**kwargs):
        print("hello")
        print(args)
        print(kwargs)
        func(*args,**kwargs)
        print("world")
    return hello



@extend
def tmp(a,b,c,d):
    print("tmp")

@extend
def tmp1():
    print("tmp1")



def test_wrapper_two():
    tmp(1,2,3,d=10)
    tmp1()

