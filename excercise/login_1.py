def find_duplicates(num_list):
    unique_list = []
    duplicates = []
    for i in num_list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicates.append(i)
    return duplicates

# numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]
# result = find_duplicates(numbers)
# print(result)


def non_repeating_char(text):
    unique_char = ""
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            unique_char += char

    return unique_char

# text = "swiss"
# print(non_repeating_char(text))


def second_largest_number(num_list):
    largest = second_largest = float('-inf')
    for num in num_list:
        if num > largest:
            largest = num
            second_largest = largest
        elif num > second_largest or num != largest:
            second_largest = num
    return second_largest

# numbers = [10, 5, 20, 8, 15]
# print(second_largest_number(numbers))


def group_list_of_dictionary(users):
    new_dict = dict()
    for user in users:
        if user['department'] not in new_dict:
            new_dict[user['department']] = list(user['name'])
        else:
            new_dict[user['department']].append(user['name'])
    return new_dict

# users = [
#     {"name": "A", "department": "IT"},
#     {"name": "B", "department": "HR"},
#     {"name": "C", "department": "IT"},
#     {"name": "D", "department": "HR"},
# ]
# groups = group_list_of_dictionary(users)
# print(groups)


def flatten(list_list):
    new_list = []
    for i in list_list:
        if isinstance(i, list):
            new_list.extend(flatten(i))
        else:
            new_list.append(i)
    return new_list

# data = [1, [2, 3], [4, [5, 6]], 7]
# print(flatten(data))


##################
# Write a Python decorator for execution time
##################
# import time
# from functools import wraps
# def timer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         print("end")
#         end = time.perf_counter()
#         exec_time = end - start
#         print(f"{func.__name__} took {exec_time} seconds")
#         return result
#     return wrapper
#
# @timer
# def process_data():
#     time.sleep(2)
#     return "Processed Completed"
#
# result = process_data()
# print(result)


##############
##LRU Cache
##############
# from _collections import OrderedDict
#
# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#
#         self.cache.move_to_end(key)
#         return self.cache[key]
#
#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#
#         self.cache[key] = value
#
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)
#
#
# cache = LRUCache(2)
# cache.put(1, 'A')
# cache.put(2, 'B')
#
# print(cache.get(1))
# print(cache.get(2))
#
# cache.put(3, 'C')
# print(cache.get(3))
# print(cache.get(2))
# print(cache.get(1))