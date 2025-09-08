# Q9. Majority Element
# Check if an element occurs more than n/2 times in a list.

from collections import Counter
ls = [4,5,6,7,4,5,4,5,4,4,4]
c = Counter(ls)
print(c)
if c.most_common(2)[0][1] > len(ls)//2:
    print(f"Majority element is {c.most_common(1)[0][0]}")
else:
    print("No majority element")
