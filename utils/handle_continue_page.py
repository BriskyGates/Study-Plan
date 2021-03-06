# 专门用来处理分页
from utils.single_link import SingleLinkedList

data = [ 4, 5, 6]
# b = [[2, 2], [4, 5], [8, 8]]

# data = [1, 4, 5, 6, 8]
# c = [[1, 1], [4, 6], [8, 8]]

final_result = []
index = 0
while index < len(data):
    sing = None
    if index == len(data) - 1:
        final_result.append(SingleLinkedList(data[index]))
    elif data[index] + 1 == data[index + 1]:
        flag = False
        index_begin = index
        while True:
            index += 1
            index_end = index
            if data[index] + 1 == data[index + 1]:
                index_end = index
            else:
                break
        sing = SingleLinkedList()
        for continual_ele in data[index_begin:index_end + 1]:
            sing.append(continual_ele)
        final_result.append(sing)
    else:
        sing = SingleLinkedList(data[index])
        final_result.append(sing)
    index += 1
pass
