"""user_input = input("Введите число")  альтернативное решение task 3

if not user_input.isdigit():
    print("Неизвестный формат числа")
    exit()

result = 0

for x in range(1, 4):
    result += int(user_input * x)  # ‘3’ * 2 =33  так как user_input является строкой то допустим введённая 3 при умножении на 2 будет 33
print(result)


Второе решение
user_number = int(input("Введите число"))  #альтернативное решение task 3

if not user_input.isdigit():
    print("Неизвестный формат числа")
    exit()

characters_cont = 0 #здесь будем считать количество цифр
temp_number = user_number #создаем временную переменную для хранения того что ввел юзер

while temp_number: # цикл пока существует число temp_number - здесь мы считаем кол-во символов в числе заданным пользователем деля его каждый раз на 10 и забирая целый остаток.
    temp_number //= 10 # это более краткая версия записи temp_number = temp_number // 10
    characters_cont += 1"""

my_dict = {"key_1": 500, 2: 400, "key_3": True, 4: None}

# popitem
print(my_dict.popitem())
print(my_dict.popitem())
print(my_dict.popitem())
print(my_dict.popitem())

