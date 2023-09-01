even_squares = (x ** 2 for x in range(10) if x % 2 == 0)

for value in even_squares:
    print(value)  # Output: 0, 4, 16, 36, 64
