is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("you are male but not tall")
else:
    print("You are not male and not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 4000, 5))

print("======while loop=======")

i = 0
while i < 10:
    print(i)
    i = i + 1

print("======for loop=======")

for letter in "one":
    print(letter)

friends_list = ("arul", "partha", "kevin", "vathi")

for friend in friends_list:
    print(friend)

for idx in range(len(friends_list)):
    print(friends_list[idx])

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)


def raise_to_power(base_num, power):
    result = 1
    for idx2 in range(power):
        result = result * base_num
    return result


print(raise_to_power(2, 5))


