# Exercise 1

# numbers_list = list(map(int, input().split(" ")))
#
# numbers_sum = 0
# numbers_count = 0
# final_list = []
# count = 0
#
# for number in numbers_list:
#     numbers_sum += number
#     numbers_count += 1
#
# average_of_numbers = numbers_sum / numbers_count
#
# for i in reversed(sorted(numbers_list)):
#
#     if i > average_of_numbers:
#         if count <= 4:
#             final_list.append(i)
#         else: break
#     else: break
#     count += 1
#
# string_list = list(map(str, final_list))
# result = " ".join(string_list)
#
# if len(string_list) <= 1:
#     print("No")
# else: print(result)

# Exercise 2

# number_list = list(map(int, input().split(" ")))
# command = input()
# empty_list = []

# while command != "end":
#     if command == "decrease":
#         number_list = list(map(lambda n: n - 1, number_list))
#     else:
#         explode = command.split(" ")
#         action = explode[0]
#         index1 = int(explode[1])
#         index2 = int(explode[2])
#         if action == "swap":
#             number_list[index1], number_list[index2] = number_list[index2], number_list[index1]
#         if action == "multiply":
#             number_list[index1] = number_list[index1] * number_list[index2]
#
#
#     command = input()
#
# for_print = list(map(str, number_list))
# result = ", ".join(for_print)
# print(result)

# Exercise 3

# Taking user input
# worker1_efficiency, worker2_efficiency, worker3_efficiency = int(input()), int(input()), int(input())
# students_count = int(input())
#
# # Declaring variables for our logic
# combined_work_per_hour = worker1_efficiency + worker2_efficiency + worker3_efficiency
# counter_hour = 0
# hour_spent = 0
#
# # Logic
#
# while students_count > 0:
#     hour_spent += 1
#     counter_hour += 1
#
#     students_left = students_count - combined_work_per_hour
#     students_count = students_left
#
#     if counter_hour % 4 == 0:
#         counter_hour +=1
#         hour_spent += 1
#         continue
#
# print(f"Time needed: {hour_spent}h.")





