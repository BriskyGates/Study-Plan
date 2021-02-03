from configparser import ConfigParser


class CfgOperation():
    def __init__(self, config_name, section):
        self.config_name = config_name  # cfg 文件文件夹
        self.cf = ConfigParser()
        self.section = section

    def read_config(self):
        """
        Returns: 以字典形式返回该section 下所有键值对

        """
        self.cf.read(self.config_name, encoding='utf-8')
        section_properties = self.cf.items(self.section)
        info = {key: value for key, value in section_properties}
        return info


if __name__ == '__main__':
    CfgOperation('ssh_config.cfg', 'ssh').read_config()
