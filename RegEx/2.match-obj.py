''' 
The match object returned by the 'seach()' function provides a lot of information, and it can be viewed using the functions 'span()', 'start()', and 'end()'

'''

import re

pattern = 'cat'
string = 'My Favourite animal is cat.'

match =  re.search(pattern, string)
s = match.start()
print(s)
e = match.end()
print(e)
sp = match.span()
print(sp)
sp1 = match.span() [0]
print(sp1)
sp2 = match.span() [1]
print(sp2)

print(f'The pattern {match.re.pattern} is found in {match.string} from {s} to {e} (\'{string[s:e]}\')')
