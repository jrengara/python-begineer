import math


def say_hi(name, age):
    print("hello " + name + "and age - " + str(age))


say_hi("mike", 55)
say_hi("mike2", 70)


def cube(n):
    return math.pow(n, 3)


print(cube(2))
print(cube(3))
print(cube(4))

result = cube(10)
print(result)

print(3**3)

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter input phrase : ")))

