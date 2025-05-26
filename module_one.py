if __name__ == "__main__":
    print("this is main")


# Example of unpacking with a list
numbers: list[int] = [1, 2, 3, 4, 5]
a, b, *other ,last = numbers
print(a)  # Output: 1
print(b)  # Output: 2
print(other)  # Output: [3, 4]
print(last)  # Output: 5
print(type(b))

# Example of unpacking with a tuple
names: tuple[str] = ("Alice", "Bob", "Charlie", "David")
a, b, c, last = names
print(a)  # Output: Alice
print(b)  # Output: Bob
print(c)  # Output: Charlie
print(last)
print(type(last))


