import re

PDF_SUFFIX_PATTERN = '*.[pP][dD][fF]'
TIME_FORMAT = 'YYYYMMDD-HHmmss'
PATTERN_PURE_DIGIT = re.compile('(\d*[\.,]?\d*[,\.]?\d+)')  # 提取纯数字正则模式
USELESS_CH=['’', "'", '[\u4e00-\u9fa5]', ' ']
if __name__ == '__main__':
    temp = 12288
