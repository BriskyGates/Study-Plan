def get_continual_page(data):
    final_result = []
    index = 0
    length_data = len(data)
    while index < length_data:  # 判断当前长度是否越界
        if index == length_data - 1:  # 此时访问到最后一个元素
            final_result.append([data[index]] * 2)  # 列表最后一个元素自成一页
        elif data[index] + 1 == data[index + 1]:  # 判断下一页是否为当前页的续页,<a>
            index_begin = index  # 以当前页作为续页的开始,便于下面取续页的首尾两页的下标
            index += 1
            index_end = index  # 每次判断下一页为当前页<a>的续页,就把续页的结束页赋值给index_end
            while True:  # 通过循环得出连续页的下标
                if index == length_data - 1:  # 如果访问到最后一个元素,则跳过当前循环,不然下一行代码会报错
                    break
                if data[index] + 1 == data[index + 1]:
                    index_end = index + 1
                else:  # 下一个元素不是当前页续页则跳出循环
                    break
                index += 1
            final_result.append([data[index_begin], data[index_end]])
        else:
            final_result.append([data[index]] * 2)  # 除尾页以外的其他页存在不连续
        index += 1
    return final_result


if __name__ == '__main__':
    data = [2, 4, 5, 6, 8]
    final_result = get_continual_page(data)
    print(final_result)
