"""
为了防止函数经过装饰器修饰后，func.__name__ 发生变化（变成了wapper），标准装饰器如下
"""
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
