''' 
The 'match()' function:
	The match() function is used to search the pattern only at the beginning of a string. The re.match function returns a match object on success, None on failure.

Syntax:
	re.match(pattern, string, flags = 0)
'''

import re

pattern = 'cat'
string = 'My Favourite animal is cat.'

print('String		:', string)
print('Pattern	:', pattern)

match =  re.match(pattern, string)
print('If any match found? : ', match)

string2 = 'cat is my favourite animal.'
print('String		:', string2)
print('Pattern	:', pattern)
match2 =  re.match(pattern, string2)
print('If any match found? : ', match2)
