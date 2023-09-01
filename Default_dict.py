from collections import defaultdict

name_age = defaultdict(int)
name_age['Person1'] = 20

print(name_age['Person1'])  # Output: 2o
print(name_age['Bob'])    # Output: 0 (default value for int)
