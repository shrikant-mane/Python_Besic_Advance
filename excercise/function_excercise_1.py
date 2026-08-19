def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

# print(max_of_three(5, 6, 7))
# print(max_of_three(4,7,5))


def rev_string(string):
    """
    reverse string
    :param string:
    :return:
    """
    list_str = list(string)
    i =0
    j = len(list_str)-1
    temp = ""
    while i<j:
        temp = list_str[i]
        list_str[i] = list_str[j]
        list_str[j] = temp
        i+=1
        j-=1
    new_string = ""
    for i in list_str:
        new_string += i
    return new_string
# print(rev_string("abcde"))


def is_prime_number(number):
    """
    check prime number
    :param number:
    :return:
    """
    if number <= 1:
        is_prime = False
    else:
        i = 2
        is_prime = True
        while i <= (number//2+1):
            if number % i == 0:
                is_prime = False
                break
            i +=1
    if  is_prime :
        return True
    else:
         return False
# print(is_prime_number(15))


def is_perfect_number(number):
    """
    to find whether a number is perfect or not
    :param number:
    :return:
    """
    sum = 0
    i = 1
    while i < (number//2+1):
        if number % i ==0:
            sum += i
        i +=1
    if sum == number:
        return True
    else:
        return False

# print(is_perfect_number(5))
# print(is_perfect_number(6))
# print(is_perfect_number(28))


def is_palindrome(string):
    """
    check whether a string is a palindrome
    :param string:
    :return: bool
    """
    rev_string = string[::-1]
    if rev_string == string:
        return True
    else:
        return False
# print(is_palindrome('madam'))
# print(is_palindrome('racecar'))
# print(is_palindrome('hello'))


def pasclas_triangle(n):
    trow = [1]
    y = [0]

    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    return n>=1

# pasclas_triangle(5)


def is_pangram_string(string):
    """
    check pangram string
    :param string:
    :return:
    """
    std_str = 'abcdefghijklmnopqrstuvwxyz'

    str_new = ''
    for i in string:
        if i not in str_new:
            str_new += i

    if len(str_new) == len(std_str):
        return True
    else:
        return False
#string = "abcdefghijklmnopasdrqrstuvwxyzasdrtg"
# print(is_pangram_string(string))


def order_str(str_list):
    """
    Sort Hyphen-Separated Sequence of Words Alphabetically
    :param str_list:
    :return: string
    """
    list_str = str_list.split("-")
    data = list(sorted(list_str))
    out_str = "-".join(data)
    return out_str

# input_str = "green-red-yellow-black-white"
# print(order_str(input_str))


