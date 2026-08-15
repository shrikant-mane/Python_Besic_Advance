from itertools import chain

def list_with_index(list_str):
    x = len(list_str)
    for i in range(x):
        print("{}....{}....{}".format(list_str[i], i, i-x))

list_with_index([9,7,6,5,4])


def list_operations(list_obj):
    """
    operations on list object
    :param list_obj:
    :return:
    """
    print(list_obj)
    print(len(list_obj))
    print(list_obj.count(2))
    print(list_obj.index(5))

    list_obj.insert(1,55)
    print(list_obj.pop())
    list_obj.pop(2)
    print(list_obj)
    list_obj.remove(7)
    print(list_obj)
    list_obj.reverse()
    print(list_obj)
    list_obj.sort(reverse=True)
    print(list_obj)
    list_obj.clear()
    print("list_obj",list_obj)


list_operations([7,2,4,2,7,5])

def flatter_list(nested_list):
    """
    flatten nested list
    :param nested_list:
    :return: flattened list
    """

    # flat_list = [item for sublist in nested_list for item in sublist]
    # return flat_list
    flat_chain_list = list(chain.from_iterable(nested_list))
    return flat_chain_list

flat_list = flatter_list([[1,2,3],[4,5,6], [7,8]])
print("Flat_list",flat_list)


def reverse_list(students):
    students.sort(key=lambda student: student[1], reverse=True)
    return students

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
data = reverse_list(students)
print(data)

def reverse_str_list(str_list):
    str_list.sort(key=len)
    return str_list

data = reverse_str_list(['aawedr', 'bb', 'cccc', 'cdf'])
print(data)


