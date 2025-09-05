#basically json hi hai
person = {"name": "Atishay", "age": 18, "mood": "sleepy"}
print("Person info:", person)
print("Name:", person["name"])
print("Age:", person["age"])
print("Mood:", person["mood"])
person["mood"] = "energetic"
print("Updated mood:", person["mood"])
person["city"] = "New York"
print("Added city:", person["city"])
print("All keys:", person.keys()) #weird sa hai to we use list() to convert to list
print("All values:", list(person.values())) #yess now its better
#ab i want to print them all without square brackets

print("All items:", list(person.items()))
for key, value in person.items(): #.items() returns key value pairs as tuples in a list
    print(f"{key}: {value}")
print("Number of entries in person dictionary:", len(person))
#i guess ye username password ke liye use hota hoga, par fir. SQL ka kya kaam 
# kya pata seekhenge aage chalke