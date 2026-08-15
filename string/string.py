###================
## Program to display all positions of substring in a given main string
###===============
#
# main_str = "abcdabcdabcababcd"
# sub_str = 'abc'
#
# main_length = 0
# for ch in main_str:
#     main_length += 1
#
# sub_length = 0
# for ch in sub_str:
#     sub_length += 1
#
# found = False
#
# i =0
# while i <= main_length - sub_length:
#     j = 0
#     while j < sub_length:
#         if main_str[i+j] != sub_str[j]:
#             break
#         j += 1
#     if j == sub_length:
#         found = True
#         print(i)
#     i += 1
# if found == False:
#     print("no")
from sys import flags

# string = "abderfdedcbf"
#
# char_dict = {}
# for i in string:
#     if i not in char_dict.keys():
#         char_dict[i] = 1
#     else:
#         char_dict[i] += 1
#
# print(char_dict)

# shrikant = "shrikant"
# new_str = shrikant[:2] + shrikant[len(shrikant)-2 : len(shrikant)]
# print(new_str)

# string = "abcdfabc"
# new_str = ""
# flag = False
# for i in string:
#     if i not in new_str:
#         new_str += i
#     elif flag == True:
#         new_str += i
#     else:
#         new_str += "$"
#         flag = True
#
# print(new_str)


class Outer:
    def __init__(self):
        print("outer init")
    class Inner:
        def __init__(self):
            print("inner init")

        def m1(self):
            print("inner m1 method")

o = Outer()
i = o.Inner()
i.m1()