# def list_difference(list1, list2):
#     set_1 = set(list1)
#     set_2 = set(list2)
#     set_difference = set_1 - set_2
#     return list(set_difference)
#
#
#
# list_1 = [int(item) for item in (input("enter list one:").split(","))]
# list_2 = [int(item) for item in (input("enter list two:").split(","))]
#
# result = list_difference(list_1, list_2)
# print(sorted(result))


#
# def intersection_array(array_list):
#     set__intersection = set(array_list[0])
#     for i in array_list:
#         temp_array = set(i)
#         set_intersection =  temp_array & set__intersection
#
#     return set_intersection
#
# array = [[1, 2, 3,4], [2, 3, 4], [3, 2,4,9]]
#
# data = intersection_array(array)
# print(data)


#
# def longest_consecutive(nums):
#     num_set = set(nums)
#     longest_streak = 0
#
#     for num in num_set:
#         if (num -1) not in num_set:
#             current_num = num
#             current_streak = 1
#
#         while (current_num + 1) in num_set:
#             current_num += 1
#             current_streak += 1
#
#         longest_streak = max(longest_streak, current_streak)
#     return longest_streak
#
# nums = [100, 4, 200, 1, 3, 2]
#
# print("longest streak: ", longest_consecutive(nums))
#

def contain_duplicate(list_num, k):
    num_set = set(list_num)
    for i in list_num:
        if i in list_num[list_num.index(i)]:pass




list_num = [int(item) for item in input().split(",")]
k = int(input("enter the number  for difference check"))

result = contain_duplicate(list_num, k)


