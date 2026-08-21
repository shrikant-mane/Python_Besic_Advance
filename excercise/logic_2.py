## Anagram string
def group_anagrams(str_list):
    """Anagram string """
    anagram = {}
    for word in str_list:
        key = "".join(sorted(word))
        if key not in anagram:
            anagram[key] = []

        anagram[key].append(word)

    return list(anagram.values())

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(words))


def find_missing_number(num_list):
    num_new_list = list(sorted(num_list))
    max_num = max(num_new_list)
    sorted_list = [i for i in range(max_num)]
    not_find = []
    for num in sorted_list:
        if num not in num_new_list:
            not_find.append(num)
    return not_find

# num_list = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# print(find_missing_number(num_list))


def rotate_list_by_k_position(num_list, k):
    split_left = num_list[:k+1]
    split_right = num_list[k+1:]
    new_list = split_right + split_left
    return new_list

# numbers = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# print(rotate_list_by_k_position(numbers, k))


def longest_consequtive_sequence(num_list):
    sorted_list = sorted(num_list)
    new_list = []
    num = sorted_list[0]
    i = 0
    while i <= len(sorted_list) - 1:
        if num in sorted_list:
            new_list.append(num)
            num +=1
            i += 1
        else: break
    return new_list

# num_list = [100, 4, 200, 1, 3, 2,5,199,23,6]
# print(longest_consequtive_sequence(num_list))


def is_balanced(expression):
    stack = []
    pairs = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for char in expression:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

# print(is_balanced("{[()]}"))   # True
# print(is_balanced("{[(])}"))   # False
# print(is_balanced("()[]{}"))   # True
# print(is_balanced("([{}])"))   # True
# print(is_balanced("([)]"))     # False
# print(is_balanced("((("))      # False
# print(is_balanced(""))         # True


def pair_with_given_sum(num_list, target):
    new_list = []
    for num in num_list:
        value = target - num
        if value in num_list:
            list_temp = [num, value]
            if tuple(list_temp[::-1]) not in new_list:
                new_list.append(tuple(list_temp))
                list_temp = []
    return new_list

# numbers = [2, 7, 11, 15, 3, 6]
# target = 9
# print(pair_with_given_sum(numbers, target))


def value_in_set(set_data, num):
    list_data = list(set_data)
    flag = False
    for i in list_data:
        if i == num:
            flag = True

    return flag
# set_data = {3,4,6,5,3}
# number = 6
# print(value_in_set(set_data, number))


def is_comman_element(set_1, set_2):
    new_set = set()
    new_set = set_1.intersection(set_2)
    list1 = list(set_1)
    list2 = list(set_2)
    for i in list1:
        if i in list2:
            new_set.add(i)
    return new_set

# set_1 = {1,2,3,4}
# set_2 = {5,2,7,8}
# print(is_comman_element(set_1, set_2))
