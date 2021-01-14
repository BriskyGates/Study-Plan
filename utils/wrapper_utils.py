from functools import wraps


def check_empty(return_value="*"):
    def first_deco(func):
        @wraps(func)
        def wrapper(self, data: list):  # 适用于类的检查传入参数是否为空
            # 去除args 中的空字符串
            new_args = list(filter(None, data))  # 去除data 中的空字符串
            if not new_args:  # 直接传入filter 对象不行, 必须经过list() 函数处理
                return return_value
            result = func(self, new_args)
            return result

        return wrapper

    return first_deco
