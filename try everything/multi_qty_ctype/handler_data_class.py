import re

from multi_qty_ctype.loguru_utils import LoguruUtil
from multi_qty_ctype.universal_constant import USELESS_CH


class HandleData():
    LoguruUtil('.', 'handler_data_cluster.log').loguru_main()

    @staticmethod
    def check_no_data(*args):
        """
        实现检查arg 多列表中的各个列表是否存在空列表
        :param data_list:
        :return:
        """
        for i in args:
            if not i:  # 检查i 是否为空列表
                return False
        return True

    def return_sorted_item(self, data: dict) -> str:
        """
        1. 先根据字典的键进行排序,确保container_no始终在前,container_Qty和container_type在后
        2. 按顺序取出每个键对应的值, 并将值拼接起来
        3. 将步骤2 得到的字符串中的 无用字符删除掉
        Args:
            data:

        Returns:

        """
        data_tuple = sorted(data.items(),
                            key=lambda item: item[0])  # 按照键排序,
        values_list = [each_one for _, each_one in data_tuple]
        old_merge_data = ' '.join(values_list)
        merge_data = self.delete_useless_sub(old_merge_data, USELESS_CH)
        return merge_data

    def delete_useless_sub(self, data, pattern):
        # logger.info(f'未经处理的data为{data}')
        delimiter_after = '|'.join(pattern)
        # print(f'生成的pattern为{delimiter_after}')
        new_data = re.sub(delimiter_after, '', data, flags=re.I)
        # logger.info(f'去除多余符号后的新data为{new_data}')
        return new_data

    def delete_useless_symbol(self, data: str, pattern):
        """
        把data 中符合pattern的字符替换成空格
        """
        for i in pattern:
            data = data.replace(i, '')
        return data

    def form_regex_pattern(self, data_list):
        pattern_list = [f'{key}' for key in data_list]
        pattern_res = '|'.join(pattern_list)
        return pattern_res


if __name__ == '__main__':
    hd = HandleData()
