def sub_generator():
    yield 2
    yield 3

def main_generator():
    yield 1
    yield from sub_generator()

for value in main_generator():
    print(value)  # Output: 1, 2, 3
