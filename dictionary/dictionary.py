from collections import Counter

# def dict_operations(dictionary):
#     print(dictionary.items())
#     print(type(dictionary.items()[1]))
#     print(dictionary.keys())
#     print(dictionary.values())
#     print(dictionary.get('name'))
#     dictionary.update({'name':'Vinay'})
#     print(dictionary)
#
# dict_obj = {'name': 'shrikant', 'village':'Rajache Kurle', 'dist':'Satara'}
# dict_operations(dict_obj)


def create_dict(name_list):
    name_dict = {}
    for name in name_list:
        if name not in name_dict.keys():
            name_dict[name] = 1
        else:
            name_dict[name] = name_dict[name] + 1
    return name_dict

items = ["pen", "pencil", "pen", "eraser", "pen", "pencil"]
name_dict = create_dict(items)
print(name_dict)


def dict_counter(name_dict):
    dict_counter = Counter(name_dict)
    print(dict_counter.most_common(3))
    print(list(dict_counter.elements()))

dict_counter(name_dict)




nums = [2,7,9,11]
target = 9
print(twoSum(nums, target))