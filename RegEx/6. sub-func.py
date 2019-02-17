''' 
Using the regular expressions, you can also modify the strings using the 'sub()' function. The sub() func can be used to replace all the occurrences of a pattern with another string.

Syntax:	re.sub(pattern, replacement, string, count = 0)
'''

import re

string = 'My Favourite animal is cat. A cat is a very cute animal.'

out = re.sub("cat", "dog", string)

print(out)
