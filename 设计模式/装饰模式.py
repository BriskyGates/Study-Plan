from functools import wraps


def with_log(func):
    """
    Doubt:
        装饰器是如何处理self 实例对象问题
        a1: args 为元组,args[0] 为实例对象
    Args:
        func:

    Returns:

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__ + ' was called ' + '\nparmas: %s, %s' % (str(args), str(kwargs)))
        return func(*args, **kwargs)

    return wrapper


class Add(object):

    def __init__(self):
        self.name = 'add'

    @with_log
    def a_b(self, a, b):
        return a + b


if __name__ == '__main__':
    add = Add()
    c = add.a_b(10, 23)
    print(c)
