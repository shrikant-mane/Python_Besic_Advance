


def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after execution")
    return wrapper

@my_decorator
def greet():
    print("Hello Dev")

greet()


##===============
## Calculate Execution Time
##===============

