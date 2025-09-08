# Q7. Check String Content
# Given a string s, check:
# s.isalpha()
# s.isdigit()
# s.isalnum()

def check_string_content(s):
    return {
        "is_alpha": s.isalpha(),
        "is_digit": s.isdigit(),
        "is_alnum": s.isalnum()
    }
result = check_string_content("Hello123")
print(result)
