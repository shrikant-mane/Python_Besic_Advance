"""
You can pass multiple exceptions of same parent class can pass into the
single exception block
"""

try:
    result = 10 / 0

except (ZeroDivisionError, OverflowError, FloatingPointError):
    print("Arithmetic exception")


# order

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Zero division")

except ArithmeticError:
    print("Other arithmetic error")

except Exception:
    print("Other exception")


