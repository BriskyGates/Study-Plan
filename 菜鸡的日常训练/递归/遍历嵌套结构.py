"""
思想:
     当大问题和小问题的解决方法是一样时, 将大问题不断地分解成`规模更小`的子问题，
     直到该子问题归约成可以直接得到`子答案`，然后通过递归退层合并子问题的答案
实现思路:
    1. 利用切片不断操作一个大列表, 确保得到的新列表为除第一个元素外其他元素的列表
    2. 检查第一步得到新列表是否为列表类型, if so, 再进行递归操作
"""

def reverse_list(alist):
    if alist != []:
        reverse_list(alist[1:])  # 切片得到是列表哦,将除第一个元素外的其他元素放在一个列表中
        if type(alist[0]) == list:  # alist可能是个列表套列表
            reverse_list(alist[0])
        else:
            print(alist[0], end="   ")

if __name__ == '__main__':

    list1 = [[1, 55], [2, 3]]  # [1, [2, 3], 4, [5, 6, [7, 8], 9]]
    reverse_list(list1)
