'''
The re.search() function is used to search fr a pattern in a string. It takes the string as the input. The syntax of this function is
re.search(pattern, string [, flags])

If the search is successful, then the function returns a match object else it returns 'None'. The match object returned by the 'search()'
function provides the information about the nature of match and the location in the string where the pattern occurs.
'''

import re

patterns = ['cat', 'dog']

string = 'My favourite animal is cat.' 

for pattern in patterns:
	print('finding {} in {} ->'.format(pattern, string))
	if re.search(pattern, string):
		print('Match Found!')
	else:
		print('No Match Found!')
