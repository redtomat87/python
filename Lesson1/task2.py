user_time = int(input("Введите время в секундах >> "))
minute = user_time // 60
hours = minute // 60
ostatokMinut = user_time % 3600
minute_ostatok = ostatokMinut // 60
print(f"{user_time} секунд это {minute} минут или {hours} часов и {minute_ostatok} минут.")
