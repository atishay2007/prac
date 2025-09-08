
from collections import Counter
el = ['a','b', 'c', 'a', 'b', 'a', 'f', 'f', 'f', 'f']
c = Counter(el)
print(c)
print(sorted(el, key=lambda x: (-c[x], x)))  
# ['f', 'f', 'f', 'f', 'a', 'a', 'a', 'b', 'b', 'c']