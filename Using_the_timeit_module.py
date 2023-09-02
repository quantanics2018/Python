import timeit

code_to_measure = """
# Your code here
a=10
b=10
c=a+b
print(c)
"""

elapsed_time = timeit.timeit(stmt=code_to_measure, number=1000)
print(f"Average time per loop: {elapsed_time / 1000} seconds")
