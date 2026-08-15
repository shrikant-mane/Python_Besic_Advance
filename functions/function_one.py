## positional and default argument

# def greet(name, age=27):
#     print(f"Hello {name}, you are {age} years old")
#
#
# greet('shrikant')   # positional
#
# greet('Vinay', 28)  # positional and default
#
# ## *args --> any number of positional arguments
# ## **kwargs  --> any number of keyword arguments {key: value}
#
# def addition(*numbers):
#     return sum(numbers)
# result = addition(1,2,3,4)
# print(result)


# # function to print keyword arguments
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# # pass any number of keyword arguments
# greet(name="John", greeting="Hello")


# global_var = 'global'
# def types_variables():
#     message = "message_local"
#     def inner():
#         nonlocal message
#         message = "message_nonlocal"
#         print("inner: ", message)
#
#     inner()
#     print("outer: ", message)  # --> message_nonlocal
#
# types_variables()


# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(5))


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# num =5
# if num == 0:
#     print("number should be greater than 0")
# else:
#     for i in range(num):
#         print(fibonacci(i))

#
# def person_info(name, age, **kwargs):
#     """
#     for display the person info
#     having positional and default arguments
#     """
#
#     print(f"Name: {name}, Age: {age}")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# person_info("John", 42, department="IT", id=23)


# def apply_operations(x,y, operation):
#     """
#     performs the operations on the given values
#     :param x:
#     :param y:
#     :param operation:
#     :return: applied operation out put
#     """
#     return operation(x, y)
#
# def add(x,y):
#     return x + y
#
# def subtract(x,y):
#     return x - y
#
# result = apply_operations(3,4, add)
# print(result)

#
# def int_addition(num1:int, num2:int):
#     if not isinstance(num1, int) or not isinstance(num2, int):
#         raise "Both numbers must be integers."
#     return num1 + num2
# print(int_addition(3,4))
# print(int_addition(3,4.5))