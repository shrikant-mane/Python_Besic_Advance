def Armstrong_number(number):
    """
    Using built-in function
    :param number:
    :return:
    """
    num_len = len(str(number))
    result = 0
    for num in str(number):
        result += int(num)**num_len

    print(result)
    if number == result:
        return True
    else:
        return False

print(Armstrong_number(155))


def ArmstrongNumber(number):
    """
    without built-in function
    :param number:
    :return:
    """
    digit = number
    len = 0
    while digit > 0:
        digit = digit//10
        len += 1
    print(len)

    temp = number
    result = 0
    while temp > 0:
        num = temp % 10
        result += num**len
        temp = temp // 10
    return result

result = ArmstrongNumber(155)
print(result)




