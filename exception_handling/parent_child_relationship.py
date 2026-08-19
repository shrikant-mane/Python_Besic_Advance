"""
if by "parent-child relationship" you mean parent class and child class, then exception
handling itself doesn't automatically propagate because of inheritance.
"""

class Parent:
    def process(self):
        raise ValueError("Error in parent")

class Child(Parent):
    pass

obj = Child()

try:
    obj.process()
except ValueError as ex:
    print(ex)


# Child overrides parent method
class Parent:
    def process(self):
        try:
            print("Parent Processing")
        except Exception:
            print("Parent Exception")


class Child(Parent):
    def process(self):
        raise ValueError("child error")


obj = Child()

try:
    obj.process()
except ValueError as ex:
    print("Caller handled : ", ex)

"""
In Python, exceptions propagate up the call stack. If an exception occurs in a child 
function and the child doesn't handle it, Python searches for a matching exception 
handler in the caller, then continues upward through the call stack. If the parent 
handles it, execution continues after the parent's except block. If no handler is found, 
the program terminates with a traceback. If the child handles the exception itself, it 
doesn't propagate to the parent unless the child explicitly re-raises it using raise
"""

"""
Child
  ↓
Exception
  ↓
Child try/except?
  ↓ No
Parent try/except?
  ↓ No
Grandparent try/except?
  ↓ No
Global/Top-level handler?
  ↓ No
Program terminates
"""


