import re

# a = '2.8 1 * 20gp  2*30 hq'
# temp=re.sub(r'(\d+) *([x*]) *(\d+)([a-z]{2})',r'\1\2\3\4',a)
# print(temp)
# print(a)
temp_str = "123abc 456def"
temp_pattern = re.compile('(\d+)([A-Z]+)', flags=re.I)
temp_res = re.finditer(temp_pattern, temp_str)
for i in temp_res:
    print(i.groups())
    print(i)
"""
('123', 'abc')
<re.Match object; span=(0, 6), match='123abc'>
('456', 'def')
<re.Match object; span=(7, 13), match='456def'>
"""