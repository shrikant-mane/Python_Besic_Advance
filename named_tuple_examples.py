from collections import namedtuple

Person = namedtuple('person', ['name', 'age', 'city'])

new_person = Person(name='shrikant', age=27, city='satara')
print(new_person)


## assign default value
Person.__new__.__defaults__ = (25, 'karad')
employee = Person(name='Vinay')
print(employee)
print(employee.name)
print(employee.age)
print(employee.city)

## convert namedtuple into dictionary
Book = namedtuple('book', ['name','author', 'price'])
book = Book(name='Polity', author='Lakshmikant', price=500)
print(book)
print(book._asdict())


## update tuple
book_update = book._replace(price=1000)
print('book_update',book_update)
print(book)



Students = namedtuple('Students', ['name', 'age'])
students = [
    Students(name='Shrikant', age=27),
    Students(name='Vinay', age=25),
    Students(name='Karad', age=25),
]

for student in students:
    print(f"")