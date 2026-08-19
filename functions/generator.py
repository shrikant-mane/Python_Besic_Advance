"""
A generator is a special type of Python function that allows us to generate values one
at a time instead of creating and storing all values in memory at once.
"""

def normal_function():
    return [1,2,3,4,5]

numbers = normal_function()
print(f"numbers: {numbers}")

def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

number = generator_function()
print(f"generator number: {next(number)}")
print(f"generator number: {next(number)}")
print(f"generator number: {next(number)}")
print(f"generator number: {next(number)}")
print(f"generator number: {next(number)}")
# print(f"generator number: {next(number)}") # ==> StopIteration


"""
get_numbers()
     ↓
 yield 1
     ↓
 pause
     ↓
 next()
     ↓
 yield 2
     ↓
 pause
     ↓
 next()
     ↓
 yield 3
 
1. Produces a value
2. Pauses execution
3. Saves the function's state
4. Resumes when the next value is requested
"""

"""
list
numbers = [x for x in range(1000000)]

generator
numbers = (x for x in range(1000000))

List:
1,000,000 values
       ↓
Memory

Generator:
request → generate value
request → generate value
request → generate value
       ↓
Small memory footprint

"""