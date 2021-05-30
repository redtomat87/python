# password = input("Введите пароль >>  ")
# password_correct = "correct"
#
# if password == password_correct:
#     print("Верно")
# else:
#     print("неверно")
age = int(input("Введите возраст >> "))

if age >= 14:
    print("Пасспорт можно получить")
    if 20 <= age <= 45:
        print("Пасспорт можно поменять")
elif age <= 1:
    print("ПАсспорт будет через год")
else:
    print("Passport nelzya pomenyat")
