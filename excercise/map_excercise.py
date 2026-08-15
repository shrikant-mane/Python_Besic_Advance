"""
map(function, iterable)
"""
import resource


# def triple_number_map(list_num):
#     """
#     map number list
#     :param list_num:
#     :return:
#     """
#     new_list = list(map(lambda x: x*3, list_num))
#     return new_list
#
# list_num = [1,2,3,4,5]
# result = triple_number_map(list_num)
# print(result)


# def add_three_lists(num1, num2, num3):
#     result = list(map(lambda x,y,z: x+y+z, num1, num2, num3))
#     return result
#
# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]
# list_3 = [9,8,7,6]
# result = add_three_lists(list_1, list_2, list_3)
# print(result)


# def str_to_list(list_str):
#     """
#     convert each string inside the list to a list
#     :param list_str:
#     :return: list of string_list
#     """
#     result = list(map(list, list_str))
#     return result
# list_str = ['shrikant', 'vinay', 'kumar']
# result = str_to_list(list_str)
# print(result)


# def pow_list_map(base_list, exponent_list):
#     result = list(map(pow, base_list, exponent_list))
#     return result
#
# base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# exponent_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = pow_list_map(base_list, exponent_list)
# print(result)


# def tuple_str_int(student_data):
#     student_name = list(map(lambda x: x[0], student_data))
#     student_dob = list(map(lambda x: x[1], student_data))
#     students_data_weight = list(map(lambda x: int(x[2][:-2]), student_data))
#
#     print("student name:", student_name)
#     print("student dob: ", student_dob)
#     print("students data weight: ", students_data_weight)
#
# student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
# tuple_str_int(student_data)



