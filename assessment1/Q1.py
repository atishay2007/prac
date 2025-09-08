# Q1. String Transformations
# Given a string, perform the following:
# a) Concatenate it with another string.
# b) Remove all vowels.
# c) Reverse it.
# d) Swap uppercase ↔ lowercase.
# e) Count frequency of each character.
from collections import Counter

def string_transformations(s, concat_str):
    # a) Concatenate
    concatenated = s + concat_str
    
    # b) Remove vowels
    vowels = "aeiouAEIOU"
    no_vowels = ''.join([char for char in s if char not in vowels])
    
    # c) Reverse
    reversed_str = s[::-1]
    
    # d) Swap case
    swapped_case = s.swapcase()
    
    # e) Frequency count
    # freq_count = {}
    # for char in s:
    #     if char in freq_count:
    #         freq_count[char] += 1
    #     else:
    #         freq_count[char] = 1
    freq_count = dict(Counter(s))

    
    return {
        "concatenated": concatenated,
        "no_vowels": no_vowels,
        "reversed": reversed_str,
        "swapped_case": swapped_case,
        "frequency_count": freq_count
    }
result = string_transformations("Hello World", "!!!")
print(result)