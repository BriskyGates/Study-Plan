import decimal
import traceback

class CreateAccountError(Exception):
    """Unable to create a account error"""


class Account:
    """一个虚拟的银行账号"""

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    @classmethod
    def from_string(cls, s):
        """从字符串初始化一个账号"""
        try:
            username, balance = s.split()
            balance = decimal.Decimal(float(balance))
        except ValueError:
            raise CreateAccountError('input must follow pattern "{ACCOUNT_NAME} {BALANCE}"')

        if balance < 0:
            raise CreateAccountError('balance can not be negative')
        return cls(username=username, balance=balance)  # 竟然可以用这种方式来创建新用户


def caculate_total_balance(accounts_data):
    """计算所有账号的总余额
    """
    result = 0
    for account_string in accounts_data:
        try:
            user = Account.from_string(account_string)
        except CreateAccountError as cre:
            traceback.print_exc()
        else:
            result += user.balance
    return result


accounts_data = [
    'piglei 96.5',
    'cotton 21',
    'invalid_data',
    'roland $invalid_balance',
    'alfred -3',
]

print(caculate_total_balance(accounts_data))
"""
规定: 出现不懂问题 利用NOTACK 
NOTACK 2021年2月3日
    为何 caculate_total_balance()函数中的try...except 可以让程序执行到最后一个accounts_data数据,调用到上层
    答: 如果当前函数无法处理CreateAccountError ,则交给调用者来处理

"""