#ab ispe apne todo list banadiye to notion ka kya kaam
fruits = ["apple", "banana", "mango"]
print(fruits)
fruits.append("pineapple")
fruits.remove("banana")

for fruit in fruits:
    print(fruit)
print(fruits[0])  # Accessing first element
print(len(fruits))  # Length of the list
print("mango" in fruits)  # Check if "mango" is in the list
print(fruits[-1])  # Accessing last element
fruits.sort()  # Sort the list
print(fruits)
fruits.reverse()  # Reverse the list
print(fruits)