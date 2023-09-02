import random

# Generate random float in [0.0, 1.0)
print(random.random())

# Generate random integer in a range [a, b]
print(random.randint(1, 10))

# Random choice from a sequence
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))

# Shuffling elements of a sequence
random.shuffle(my_list)
print(my_list)

# Generating random sample without replacement
random_sample = random.sample(my_list, 3)
print(random_sample)
