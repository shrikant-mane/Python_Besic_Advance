# class School:
#     def __init__(self, *subjects):
#         self.subjects = list(subjects)
#
# class Subject:
#     def __add__(self, other):
#         return School(self, other)
#
# F1, F2 = Subject(), Subject()
# print(F1 + F2)
# print((F1+F2).__dict__)
#
#
# class Person:
#     def __init__(self, first_name, surname, age):
#         self.first_name = first_name
#         self.surname = surname
#         self.age = age
#
#     def __repr__(self):
#         return f'{self.first_name} : {self.surname} : {self.age}'
#
#     def __lt__(self, other):
#         return self.age < other.age
#
# data = [
#     {'first_name':"John", 'surname':'Smith', 'age':13},
#     {'first_name':"Anne", 'surname':'McNell', 'age':11},
#     {'first_name':'Mary', 'surname': 'Brown', 'age':14}
# ]
#
# results = [Person(**row) for row in data]
# print(results.sort())
# print(results)


class Test:
    a = 10
    def __init__(self):
        self.b = 20

    @classmethod
    def m1(cls):
        cls.a = 1000
        cls.b = 2000

t1 = Test()
t2 = Test()
print(t1.a, t1.b, t2.a, t2.b)
t1.m1()
print(t1.a, t1.b, t2.a, t2.b)
print(Test.a, Test.b)
