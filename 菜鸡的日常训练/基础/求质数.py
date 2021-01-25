# 查看2-13的质数
temp = list(
    filter(
        lambda x: all(
            x % y != 0 for y in range(2, x)
        ), range(2, 13)
    )
)
print(temp)
