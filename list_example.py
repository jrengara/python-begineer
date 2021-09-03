friends = ["friend1", "friend2", "friend3", "friend4", "friend5"]
print(friends)
print(friends[1])
other_list = ["friend1", 2, True]
print(other_list[1])
print(friends[-1])
friends[1] = "JP"
print(friends[1:3])

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends_list = ["kevin", "karan", "jim", "oscar", "toby","kevin"]

#friends_list.extend(lucky_numbers)
friends_list.append("creed")
friends_list.insert(2, "cisco")
#friends_list.remove("Jim")

print(friends_list)

print(len(friends_list))

#print(friends_list.index(42))

friends_list.pop()
print(friends_list)

#friends_list.clear()
#print(friends_list)

print(friends_list.count("kevin"))

friends_list.sort()

print(friends_list)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)


friends2 = friends_list.copy()
print(friends2)


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])
print(len(number_grid))

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)