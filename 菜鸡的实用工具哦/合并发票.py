from glob import glob
import os
from PyPDF2 import PdfFileMerger
from loguru import logger

# 常量
PDF_PATTERN = '*.pdf'


# 获取传入目录下所有的pdf文件
class InvoiceOperation():
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.pdf_list = []
        self.out_path = self.check_out_path()

    def fetch_files(self):
        self.pdf_list = glob(os.path.join(self.folder_name, PDF_PATTERN))

    def check_out_path(self):
        out_path_dir = os.path.join(self.folder_name, 'MERGE')
        if not os.path.exists(out_path_dir):  # 如果不存在合并pdf 后的文件夹,则创建
            os.makedirs(out_path_dir)
        return os.path.join(out_path_dir, 'merge.pdf')

    @logger.catch
    def merge_files(self):
        file_merger = PdfFileMerger()
        for pdf in self.pdf_list:
            file_merger.append(pdf)  # 合并pdf文件
        file_merger.write(self.out_path)

    def operate_main(self):
        """
        获取某文件夹下所有发票,将所有发票合并到一个pdf
        报销单需要和发票放在不同文件夹
        Returns:

        """
        self.fetch_files()
        self.merge_files()


if __name__ == '__main__':
    mypath = r'C:\Users\Epiphony\Documents\WXWork\1688850796666742\Cache\File\2021-02\小武 - 副本'
    mypath = r'C:\Users\Epiphony\Documents\WXWork\1688850796666742\Cache\File\2021-02\陈云涛'
    mypath = r'C:\Users\Epiphony\Documents\WXWork\1688850796666742\Cache\File\2021-02\赵其豪1月发票\审批单'
    invo = InvoiceOperation(mypath)
    invo.operate_main()
