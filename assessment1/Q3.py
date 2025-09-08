# Q3. Cyclic Prime Check
# Check if a number is a cyclic prime (all rotations of its digits are prime).

def cyclic(n):
    s = str(n)
    for i in range(len(s)):
        rotated = int(s[i:] + s[:i])
        if not is_prime(rotated):
            return False
    print(f"{n} is a cyclic prime.")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = 197
cyclic(number)