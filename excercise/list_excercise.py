def largest_number(num_list):
    """
    get largest_number in list
    :param list:
    :return:
    """
    largest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
    return largest
# print(largest_number([1, 2, 3, 4, 5, 11, 7, 8, 9, 10]))


def check_same(str_list):
    """
    Count Strings with Same Start and End
    :param str_list:
    :return:
    """
    count = 0
    for word in str_list:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
    return count
# print(check_same(['aba', 'abc', '12231', '12345431']))
