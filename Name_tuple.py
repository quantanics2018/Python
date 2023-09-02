from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
person = Person(name='Person1', age=25)

print(person.name, person.age)  # Output: Person1 25
