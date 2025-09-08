# Q2. Quadratic Equation Properties
# For an equation ax² + bx + c = 0, write code to:
# a) Find discriminant.
# b) Find sum of roots.
# c) Find product of roots.
# d) Find difference of roots.

def quadratic_properties(a, b, c):
    # a) Discriminant
    discriminant = b**2 - 4*a*c
    
    # b) Sum of roots
    sum_of_roots = -b / a
    
    # c) Product of roots
    product_of_roots = c / a
    
    # d) Difference of roots
    if discriminant >= 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        difference_of_roots = abs(root1 - root2)
    else:
        difference_of_roots = "Complex roots, difference not real"
    
    return {
        "discriminant": discriminant,
        "sum_of_roots": sum_of_roots,
        "product_of_roots": product_of_roots,
        "difference_of_roots": difference_of_roots
    }
