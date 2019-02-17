'''
In string, the 'split()' method is generally used to split the string. But when you want to get only the text without any special characters and whitesppaces, the 'split()' func from the RE module is used.

Syntax:
	re.split(pattern, string, maxsplit = 0) 
'''

import re

lines = ['Class: Python, Batches: 3, Students: 12', 'Class: C, Batches: 2, Students: 8']

for line in lines:
	print(re.split(",* *\w*: ", line))
