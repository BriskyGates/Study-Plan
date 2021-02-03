import os
from functools import wraps

import paramiko
from loguru import logger

from setting import UP_LOG_DIR, SSH_CONFIG
from utils.loguru_utils import LoguruUtil
from utils.fetch_config import CfgOperation


class SSHOperation():
    LoguruUtil(UP_LOG_DIR, 'ssh_operation.log').loguru_main()

    def __init__(self):
        self.ssh_config = CfgOperation('ssh_config.cfg', 'ssh').read_config()
        self.ssh_client = None
        self.final_result = ''
        # self.hd=HandleData()


    @logger.catch
    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(**self.ssh_config)  # 可以进行批处理, 不要每次查询都连接远程服务器
        self.ssh_client = ssh  # 通过ssh连接上linux 服务器

    def find_by_option(self, option: dict):
        """
        ACHIEVEMENT:
            对find 的命令添子弹, 例如执行查找路径,参数条件,例如-name xxx.pdf
            可能在找的时候要对一些文件名进行排除
        TIPS:
            一次性查找多个文件:  # find . -type f \( -name "*.sh" -o -name "*.txt" \)
        Args:
            find_option: find 函数的参数
        Returns:

        """

        name_list = option.get('name')  # 此处可能会传入多个参数
        if len(name_list) == 0:
            logger.error('name 参数为空哦 :<')
            return False
        find_location = option.get('location', 'data/raw_file')  # location 的默认位置为data/raw_file
        for each_naem in name_list:  # 可能需要判断each 是否有后缀名
            find_cmd = f"find {find_location} -name '{each_naem}'"
            self.ssh_client.run_shell(find_cmd)
            self.parser_result()

    def close(self):
        self.ssh_client.close()

    def parser_result(self):
        if not self.final_result:
            return False
        logger.info(f'以换行符分割前的结果: {self.final_result}')  # 可能需要解析最后结果, 不在这边解析
        final_result_list = self.final_result.split('\n')  # 即使一个字符串不存在\n, 也会变成一个列表其中的一个元素
        logger.info(f'以换行符分割前的结果: {final_result_list}')  # 可能需要解析最后结果, 不在这边解析

        len_final_res = len(final_result_list)  # 本地需要做下缓存
        if len_final_res > 1:
            logger.critical('搜索到多条记录, 我们只取第一条文件对应的服务器路径哦 :>')
        fetch_one = final_result_list[0]
        print(fetch_one)
        return fetch_one

    def check_result(self, cmd_result):
        ssh_in, ssh_out, ssh_error = cmd_result
        error_mes = ssh_error.read()
        if not error_mes:  # 如果error_mes 为空
            self.final_result = ssh_out.read().decode()  # 由byte 转换成str
            logger.info(f'最终执行结果为: {self.final_result}')  # 可能需要解析最后结果, 不在这边解析
            return True
        logger.error('无法搜索到结果哦 :<')
        return False

    def run_shell(self, cmd):
        """
        cmd_result 参数解释:
            元组数据类型
            当cmd 为cd michael 时succ_mes 为空数据,error_mes为 'bash: 第 0 行: cd: michael: 没有那个文件或目录'
            如何路径中存在特殊符号,需要加双引号才能正常搜索到
        Args:
            cmd:

        Returns:

        """
        logger.info(f'开始执行{cmd}')
        cmd_result = self.ssh_client.exec_command(cmd)
        self.check_result(cmd_result)


if __name__ == '__main__':
    ssh_config = SSH_CONFIG
    ssho = SSHOperation()
    ssho.connect()
    # cmd = 'cd dbs;ls'
    # cmd = 'find data/raw_file -name "DYR21T035 托单.*"'
    cmd = 'find ~/data/raw_file -name "InsertPic_(01-20-15-48-40).png"'
    # cmd = 'cd michael'  # bash: 第 0 行: cd: michael: 没有那个文件或目录
    ssho.run_shell(cmd)
    # print(res_ssh)
