import re

from loguru import logger

from multi_qty_ctype.handler_data_class import HandleData
from multi_qty_ctype.loguru_utils import LoguruUtil


class QTYContext():
    LoguruUtil('.', 'multi_qty_class.log').loguru_main()

    def __init__(self, data: dict):
        self.data = data
        self.hd = HandleData()  # 处理数据类
        self.final_data = {
            "container_no": [],
            "container_type": []
        }

    @logger.catch
    def merge_keys(self, ):
        # 接下来正则匹配
        merge_data = self.hd.return_sorted_item(self.data)
        logger.critical(f'合并data 字典后的字符串为:{merge_data}')
        container_no_findall = re.findall('[A-Z]{3}U[A-Z0-9]{7}', merge_data)  # 可能需要一直维护
        container_type_list = ['GP', 'HQ', 'HC']# 可能需要一直维护
        container_type_pattern = self.hd.form_regex_pattern(container_type_list)
        container_type_findall = re.findall(f'\d{{2}}(?:{container_type_pattern})', merge_data)  # 两个花括号代表花括号本身
        self.final_data["container_type"] = container_type_findall
        self.final_data["container_no"] = container_no_findall
        logger.info(container_no_findall)
        logger.info(container_type_findall)


if __name__ == '__main__':
    container_dict = {
        "container_type": "",
        "container_no": "TLLU8265846\n20HQ",
        "container_qty": "",

    }
    container_dict = {
        "container_type": "",
        "container_no": "TRHU1241296 YMAH06473020' GP  CY/CY 680BAGS 17136.000KGS 25.0000CBM",
        "container_qty": "",

    }

    # 对数据进行合并
    qty = QTYContext(container_dict)
    qty.merge_keys()
    # # final_data = qty.digest_data()
    # final_data = qty.final_data
    # print(final_data)
