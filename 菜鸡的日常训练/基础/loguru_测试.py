from loguru import logger


def handle_error(e):
    print(e)  # 系统自带的异常信息,例如 division by zero
    print('something wrong happens')


@logger.catch(message='888', onerror=handle_error)  # 捕获并处理
def func(a, b):
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


nested(0)
