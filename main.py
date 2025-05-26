numbers: list[int] = [1, 2, 3, 4, 5]
a, b, *other ,last = numbers
print(a)  # Output: 1
print(b)  # Output: 2
print(other)  # Output: [3, 4]
print(last)  # Output: 5
print(type(b))