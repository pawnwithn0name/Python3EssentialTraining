''' 
The findall() func is used to find all the instances of the pattern in the string, without overlapping. The general syntax is:

re.findall(pattern, string)


'''

import re

pattern = 'cat'
string = 'My Favourite animal is cat. A cat is a very cute animal.'

print('Using findall() func')

for match in re.findall(pattern, string):
	print(f'Found {pattern} in {string}')
print('using search() func')

if re.search(pattern, string):
	print('Match found')
else:
		print('No Match found')
