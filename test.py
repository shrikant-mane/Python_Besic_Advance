import time

# from excercise.JWT_Token_Validation import ALGORITHM



def fibonacci(num):
    a,b = 0,1
    for i in range(num+1):
        print(a, end=",")
        a,b= b, a+b

# fibonacci(10)
memo = {}

def fibonacci_recursive(num):
    if num <=1:
        return num
    if num in memo:
        return memo[num]

    memo[num] = fibonacci_recursive(num-1) + fibonacci_recursive(num-2)
    return memo[num]
#
# result = fibonacci_recursive(10)
# print(result)


"""
import jwt
import time

SECRET_KEY = '123456788765432112345678'
ALGORITHM = 'HS256'

def create_token():
    try:

        payload = {
            'user_id': 101,
            'role': 'admin',
            'exp': int(time.time()) + 3600,
        }
    except Exception as err:
        raise err

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

def decode_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )
    except Exception as ex:
        raise ex

    return payload

# result = create_token()
# print(result)
#
# payload = decode_token(result)
# print(payload)
"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

# gen = my_generator()
# print(gen)
# for i in range(8):
#     print(next(gen))


def numbers():
    yield 1
    yield 2
    yield 3

# gen = numbers()
#
# # First iteration
# for x in gen:
#     print(x)
#
# # Second iteration
# for x in gen:
#     print(x)

def decorator(func):
    def wrapper():
        print("Before function")
        x = func()
        print("Aftr wrapper")
        print(x)
        # return x
    return wrapper


@decorator
def info():
    print("Shrikant")
    return 10

# info()

def my_decor(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function name : {func.__name__}")
        x = func(*args, **kwargs)
        print(x)
        print(f"Completed: {func.__name__}")
    return wrapper

@my_decor
def my_sum(a,b):
    return a+b

result = my_sum(10,20)
print(result)