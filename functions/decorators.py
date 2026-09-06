from functools import wraps

def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after execution")
    return wrapper

@my_decorator
def greet():
    print("Hello Shrikant")

# greet()


# Decorator with arguments but without functools.wraps()
def my_sum_decor_without_wrap(func):

    def wrapper(*args, **kwargs):
        print(f"Calling function name : {func.__name__}")
        x = func(*args, **kwargs)
        print(x)
        print(f"Completed: {func.__name__}")
    return wrapper

@my_sum_decor_without_wrap
def my_sumwithout_wrap(a,b):
    return a+b

result = my_sumwithout_wrap(10,20)
print(result)
# The original function was called my_sum, but Python now sees the decorated function as wrapper.
print(my_sumwithout_wrap.__name__)
print(my_sumwithout_wrap.__doc__)



# Decorator with arguments but without functools.wraps()
def my_sum_decor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function name : {func.__name__}")
        x = func(*args, **kwargs)
        print(x)
        print(f"Completed: {func.__name__}")
    return wrapper

@my_sum_decor
def my_sum(a,b):
    return a+b

result = my_sum(10,20)
print(result)
print(my_sum.__name__)
print(my_sum.__doc__)


"""
"functools.wraps() is used in custom decorators to preserve the metadata of the original function, 
such as its name, documentation, and annotations. Without it, the decorated function appears to be 
the wrapper function."
"""


