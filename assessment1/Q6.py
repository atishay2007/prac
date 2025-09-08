# Q6. Mini Calculator
# Take two integers.
# a) Check if they are integers.
# b) Perform +, −, × operations.

def mini_calculator(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Both inputs must be integers."
    
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    
    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication
    }