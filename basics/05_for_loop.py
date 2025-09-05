#20 baar print statement likhne se acha loop lagado
for i in range(5):
    print("Iteration number", i)

# Looping over a list
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    print(animal)
# Looping with index
for index in range(len(animals)):
    print(f"Animal at index {index} is {animals[index]}")
# Looping with enumerate
for index, animal in enumerate(animals):
    print(f"Animal at index {index} is {animal}")
#so basically enumerate gives index and value both together instead of just value
#pehle humne range(len(animals)) use kiya tha jisme hume index mila 
#aur fir us index se value nikalni padti thi
#but with enumerate, we get both index and value directly

# Looping with step
for i in range(0, 10, 2):
    print(i)

# Looping backwards
for i in range(5, 0, -1):
    print(i)