nested_data = {
    "user": "Alice",
    "profile": {
        "age": 30,
        "address": {
            "city": "Mumbai",
            "pincode": 400001
        }
    },
    "active": True
}


def find_key(d, target_key):
    if target_key in d:
        return True

    for value in d.values():
        if isinstance(value, dict):
            if find_key(value, target_key):
                return True

# print(find_key(nested_data, "city"))
# print(nested_data.keys())



def find_key(d, target_key):
    if target_key in d:
        return True

    for value in d.values():
        if isinstance(value, dict):
            if find_key(value, target_key):
                return True

    return False

print(find_key(nested_data, "user"))
print(find_key(nested_data, "name"))

memo = {}


def fibonacci(n):
    # Base cases
    if n <= 1:
        return n

    # Check if the result is already in our dictionary cache
    if n in memo:
        return memo[n]

    # Recursive step: calculate and store the result in the dictionary before returning
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    # print(memo)
    return memo[n]
print(fibonacci(10))  # Computes instantly thanks to the dictionary cache!


def fibonacci(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(10))

