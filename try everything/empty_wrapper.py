from functools import wraps


class PlayFun():
    def check_empty(func):
        """
        在wrapper 方法中需要加入self 实参用来放实例对象
        Returns:

        """
        @wraps(func)
        def wrapper(self, data_str):
            if not data_str.strip():
                return ''
            result = func(self, data_str)
            return result

        return wrapper

    @check_empty
    def fun_main(self, data: str):
        print(f'I am {data}, pls call loverly')
        return '喵喵'


if __name__ == '__main__':
    # res = PlayFun().fun_main('   ')
    res = PlayFun().fun_main('shoot')
    print(res)
