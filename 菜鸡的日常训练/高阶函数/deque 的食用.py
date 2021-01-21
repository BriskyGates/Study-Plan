def merge(left, right):
    '''归并操作，使用可移动游标'''
    left_index = 0  # left序列的可移动的下标
    right_index = 0  # right序列的可移动的下标
    merged = []  # 用来存放最终排好序的元素

    while left_index < len(left) and right_index < len(right):  # 一旦 left序列 或 right序列 中的元素比较完成，就退出循环
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1  # left序列的下标向右移动一位
        else:
            merged.append(right[right_index])
            right_index += 1  # right序列的下标向右移动一位

    merged = merged + left[left_index:]  # 如果 left序列 还有没比较的元素
    merged = merged + right[right_index:]  # 如果 right序列 还有没比较的元素
    return merged


res = merge([1, 2, 3], [1.5,2.5 ,7, 9])
print(res)
