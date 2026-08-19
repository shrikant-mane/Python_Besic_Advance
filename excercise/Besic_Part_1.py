def sum_number(number):
    i =1
    sum = 0
    while i<4:
        sum = sum + int(str(number)*i)
        i += 1
    return sum
# print(sum_number(1))
# print(sum_number(2))
# print(sum_number(5))



def even_odd(number):
    if number %2 ==0:
        return "even"
    else:
        return "odd"

# print(even_odd(1))
# print(even_odd(2))


def list_histogram(items):
    """
        TO design histogram
    """
    for item in items:
        print("*"*item)
# list_histogram([2,3,6,5])


def list_to_str(user_list):
    """"
        to convert list object to string
    """
    new_string = ""
    for item in user_list:
        new_string += str(item)
    return new_string
# print(list_to_str(['a', 'b', 'c']))
# print(list_to_str([1,2,3,4]))


def lcm(a,b):
    """
    to find the lcm of two numbers
    :param a:
    :param b:
    :return: Least common multiple(LCM)
    """
    if a > b:
        z = a
    else:
        z = b

    while True:
        if z % a == 0 and z % b == 0:
            lcm = z
            break
        else:
            z += 1
    return lcm

# print(lcm(3,4))
# print(lcm(5,6))


def triple_sum_equality_rule(number):
    """
    triple sum
    if two values are equal, return sum = 0
    :param number:
    :return:
    """
    str_num = str(number)
    sum = 0
    list_num = []
    for i in str_num:
        if i not in list_num:
            sum += int(i)
            list_num.append(i)
        else:
            sum = 0
            break
    return sum
# print(triple_sum_equality_rule(989))

def triple_sum_equality_by_set(number):
    """
    using set
    :param number:
    :return:
    """
    num_set = set()
    for i in str(number):
        num_set.add(i)

    if len(num_set) == len(str(number)):
        return False
    else:
        return True

# print(triple_sum_equality_by_set(785))

## unique number check
def unique_numbers_check(num_list):
    """
    to check whether a number list is unique
    :param num_list:
    :return:
    """
    num_set = set(num_list)
    if len(num_set) == len(num_list):
        return True
    else:
        return False
# print(unique_numbers_check([1,2,3,4,5,5,7,8,9]))



