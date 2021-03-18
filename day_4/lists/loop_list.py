fruits = ["apple", "banana", "cherry", "orange"]

for fruit in fruits:
    print("I love " + fruit)

rng = range(0, len(fruits))

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(rng)

for i in rng:
    print("I love " + fruits[i])

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
[print("I love " + fruit) for fruit in fruits]

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
newFruits = ["I love " + fruit for fruit in fruits]
print(newFruits)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
newFruits = ["I love " + fruit for fruit in fruits if fruit != "apple"]
print(newFruits)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
newFruits = [fruit if fruit != "apple" else "pineapple" for fruit in fruits]
print(newFruits)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
newFruits = [fruit.upper() for fruit in fruits]
print(newFruits)