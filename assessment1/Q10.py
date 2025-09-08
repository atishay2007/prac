#Q10. String Rotations
# Given a string s, generate all possible rotations of the string.
# Also find unique rotations using different methods.

s = "asdfasdf"
all_rotations = [s[i:] + s[:i] for i in range(len(s))]
print("All rotations of the string are:", all_rotations)
print(len(all_rotations))
unique_rotations = list(dict.fromkeys((all_rotations)))
print("Unique rotations of the string are:", unique_rotations)
print(len(unique_rotations))
unique_rotations_set = set(all_rotations)
print("Unique rotations using set are:", unique_rotations_set)
print(len(unique_rotations_set))
