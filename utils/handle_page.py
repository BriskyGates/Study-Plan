def get_continual_page(data):
    final_result = []
    index = 0
    length_data = len(data)
    while index < length_data:  # 判断当前长度是否越界
        if index == length_data - 1:
            final_result.append([data[index]] * 2)  # 列表最后一个值自成一页
        elif data[index] + 1 == data[index + 1]:
            index_begin = index
            flag = True
            while flag:  # 用来得出连续页的首尾下标
                index += 1
                index_end = index
                if index >= length_data - 1:
                    break
                if data[index] + 1 == data[index + 1]:
                    index_end = index
                else:
                    break
            final_result.append([data[index_begin], data[index_end]])
        else:
            final_result.append([data[index]] * 2)  # 不连续的值自成一页
        index += 1
    return final_result


if __name__ == '__main__':
    data=[]
    final_result = get_continual_page(data)
    print(final_result)
