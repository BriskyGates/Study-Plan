import re

a = '2.8 1 * 20gp  2*30 hq'
temp=re.sub(r'(\d+) *([x*]) *(\d+)([A-Z]{2})',R'\1\2\3\4',a)
print(temp)