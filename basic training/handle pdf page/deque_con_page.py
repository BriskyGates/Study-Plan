"""
利用栈 来处理连续页
"""
from loguru import logger


def form_continue_page(transfer_deque: list):
    if len(transfer_deque) > 1:
        continue_page = [transfer_deque.pop(0), transfer_deque.pop(-1)]
        transfer_deque.clear()  # the list is mutable
        return continue_page
    else:
        return [transfer_deque.pop()] * 2


def deal_con_page_deque(data: list):
    final_result = []
    transfer_deque = []
    for ele in data:
        if len(transfer_deque) == 0:
            transfer_deque.append(ele)  # 只有一个元素直接添加进双端队列
        elif transfer_deque[-1] + 1 == ele:  # 当前页和上一页是连续的,则添加进transfer_deque中
            transfer_deque.append(ele)
        else:  # transfer_deque 长度不为0,且下一页不是当前页的续页
            final_result.append(form_continue_page(transfer_deque))
            transfer_deque.append(ele)
    else:  # 循环结束
        final_result.append(form_continue_page(transfer_deque))

    logger.info(final_result)
    return final_result


data = [2, 4, 5, 8]
# data = [1, 2, 3, 4]
deal_con_page_deque(data)
