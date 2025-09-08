# Q5. Review Cleanup
# Remove filler words ("like", "um", "uh").
# a) Count number of words.
# b) Count unique words.

s = "Hi I like so pissed uhh because I uhh like lost my keys um"

fillers = {"like", "um", "uhh", "uh"}

words = [word for word in s.split() if word not in fillers]

print(len(words))        # total words
print(words)             # words list
print(' '.join(words))   # cleaned sentence
print(list(dict.fromkeys(words)))  # unique words in order