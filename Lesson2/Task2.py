count = input("Сообщите количество элементов в списке >> ")
if count.isdigit():
    user_list = input("Сообщите элемент списка >> ")
else:
    count = input("Сообщите цифровое значекние >> ")
numbers = 1
count = int(count)
user_list = list(user_list)
while count > numbers:
    user_list.append(input("Сообщите следующий элемент списка >> "))
    numbers += 1
print(user_list)
user_list_1 = []
#user_list_1 = list(user_list_1)
"""for i in user_list:
    user_list_1.append([i])
for i in user_list:
    user_list_1.append([i])
print(user_list_1)
"""
for i in range(1, len(user_list), 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]

print(user_list)