# Q11. Valid Numbers in Range
# Print numbers in a given range that satisfy:

# No digit = 0

# Divisible by each digit

# Sum of digits divisible by 2

# Reversed number divisible by 3
s = int(input("Enter Range: "))

def valid(n):
    n_str = str(n)
    
    # No digit is 0
    if '0' in n_str:
        return False
    
    # Divisible by each digit
    for digit in n_str:
        if n % int(digit) != 0:
            return False
    
    # Sum of digits divisible by 2
    digit_sum = sum(int(digit) for digit in n_str)
    if digit_sum % 2 != 0:
        return False
    
    # Reversed number divisible by 3
    if int(n_str[::-1]) % 3 != 0:
        return False
    
    return True

result = [i for i in range(s+1) if valid(i)]
print(result)
