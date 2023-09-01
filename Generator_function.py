def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator function
for i in countdown(5):
    print(i)  # Output: 5, 4, 3, 2, 1
