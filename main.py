# text = "Hello world"
# print(text.split())
# print(text.capitalize())

#students = [
#     {
#         "name": "Jonh",
#         "presense": None
#     },
#     {
#         "name": "Jerry",
#         "presense": None
#     },
#     {
#         "name": "Jane",
#         "presense": None
#     }
# ]
# presense_count = 0
#
# for student in students:
#     flag = True
#     while flag:
#         presense_choice = input(f"Чи є {student['name']} на занятті (Y/N)")
#         if presense_choice.lower() == "y":
#             student['presense'] = True
#             presense_count += 1
#             flag = False
#         elif presense_choice.lower() == "n":
#             student['presense'] = False
#             flag = False
#         if flag:
#                 print("Ви вибрали не вірне значення, Введіть вашу відповідь щераз !\n\n")
# print(f"Присутні: {presense_count}. Відсутні: {len(students) - presense_count}")

# for item in range(2, 11, 2):
#     print(item)

# count_new_students = int(input("Введіть скільки студентів хочете додати"))
# for i in range(count_new_students):
#     name_student = input("ведіть ім'я студента: ")
#     frame_student = {
#         "name": name_student,
#         "presense": None
#     }
#     students.append(frame_student)
# print(students)
# a =0
# while True:
#     a += 1
#     if a <= 10:
#     print(a)

# b = True
# c = 0
# while b:
#     c += 1
#     if c >= 100:
#         b = False
#     print(c)

# b = True
# c = 0
# while True:
#     c += 1
#     if c >= 100:
#         continue
#     elif c >= 105:
#         break
#     print(c)

# number = 0
# while number <= 100:
#     number = int(input("Введіть число: "))
#     if number > 100:
#         print("Ви успішно ввели потрібне число! Вітаю ви можете вводити числа!")

# credit_data = {
#     'user1': {
#         'credit1': 5000,
#         'credit2': 2000,
#         'credit3': 10000
#     },
#     'user2': {
#         'credit1': 3000,
#         'credit2': 1500,
#         'credit3': 8000
#     },
#     'user3': {
#         'credit1': 7000,
#         'credit2': 0,
#         'credit3': 5000
#     },
#     'user20': {
#         'credit1': 10000,
#         'credit2': 5000,
#         'credit3': 3000
#     }
# }
# credit_one_count = 0
# credit_two_count = 0
# credit_three_count = 0
# for item in credit_data:
#     for credit in credit_data[item]:
#         if credit == "credit1":
#             credit_one_count += credit_data[item][credit]
#         elif credit == "credit2":
#             credit_two_count += credit_data[item][credit]
#         elif credit == "credit3":
#             credit_three_count += credit_data[item][credit]
# print(" аборгованість по кредиті: ", credit_one_count)
# print(" аборгованість по кредиті: ", credit_two_count)
# print(" аборгованість по кредиті: ", credit_three_count)
# max_debt = 0
# for item in credit_data:
#     total_debt =0
#     for credit in credit_data[item]:
#         total_debt += credit_data[item][credit]
#     if max_debt < total_debt:
#         max_debt = total_debt
#         user_max_debt = item
# print(f"{user_max_debt} -- {max_debt}")