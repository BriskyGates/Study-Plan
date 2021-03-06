# 专门用来处理分页
from 菜鸡的日常训练.基础.处理分页数据 import SingleLinkedList

data = [2, 4, 5, 8]
# b = [[2, 2], [4, 5], [8, 8]]

data = [1, 4, 5, 6, 8]
# c = [[1, 1], [4, 6], [8, 8]]

for index in range(len(data)):
    if data[index] + 1 == data[index + 1]:
        SingleLinkedList()
