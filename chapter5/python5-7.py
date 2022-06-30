m = [[1, 2], [3, 4], [5, 6], [7, 8]]

transpose = [[row[i] for row in m] for i in range(len(m[0]))]

print(transpose)
print()

for i in range(len(transpose)):
    print(*transpose[i])
