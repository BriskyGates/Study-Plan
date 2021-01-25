# 查看2-13的质数
temp = list(
    filter(
        lambda x: all(
            x % y != 0 for y in range(2, x)
        ), range(2, 13)
    )
)
"""
代码执行顺序:
    利用range(x,y) 提前生成需要查询质数的范围
    传入lambda 一个数
    利用第二层循环查看2,x 之间是否存在能被整除的值(会形成列表),利用all 来判断是否存在值<如果该列表存在值, 则要过滤掉>
"""
print(temp)
