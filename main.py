

""""
  list - []
        list modify - mutable

 set dict
  tuple - () - immutable

  string

  int

"""


numbers = [1,2,3,4,5]
numbers.append("shrikant")
print(numbers)


numbers = (1,2,3,4,5)

print(numbers)

name = "sagar"
print(id(name))

name = "shrikant"
print(id(name))

stundets = {
    "name": "shrikant",
    "roll_number": 30,
    "subject": "Python",
    "name": "Sagar"
}

print(stundets)


def find_addition_numbers(numbers):
    """
        function finds addition numbers
        input : numbers
        output : addition numbers
    """
    try:
        addition_numbers = 0
        for i  in numbers:
            addition_numbers += i
        return addition_numbers

    except Exception as ex:
        raise ex

result = find_addition_numbers([1,2,3,4,5])
print(result)

def greater_number(number1, number2):
    """
    function greater number
    :param number1:
    :param number2:
    :return:
    """
    try:
        if not number1 < number2:
            return number1
        else:
            return number2

    except Exception as ex:
        raise ex

#
# number1, number2 = input("enter numbers: ").split(",")
#
# result = greater_number(number1, number2)
# print(result)

def range_function():
    try:
        for i in range(10,20, 2):
            print(i)
    except Exception as ex:
        raise ex

range_function()


def odd_and_even_numbers():
    odd_numbers = []
    even_numbers = []
    try:
        for i in range(1,20):
            if i % 2 == 0:
                even_numbers.append(i)
            else:
                odd_numbers.append(i)

    except Exception as ex:
        raise ex
    return odd_numbers, even_numbers

odd_numbers, even_numbers = odd_and_even_numbers()

print(odd_numbers)
print(even_numbers)


def continue_statement():
    for i in range(1,10):
        if i == 4 or i ==7:
            continue
        print(i)

continue_statement()

def break_statement():
    for i in range(1,10):
        if i == 7:
            break
        print(i)

break_statement()

# def strip_string(string):
#     new_string = string.strip()
#     return new_string
#
# old_string = str(input("enter the string"))
#
# new_string = strip_string(old_string)
# print("stripped string: ", new_string)


def search_character(chr, string):
    length = len(string)
    i = 0
    while i < length:
        if string[i] == chr:
            return 1
        i += 1
    return 0

result = search_character('S', "HGFDSG")
print("result: ", result)
