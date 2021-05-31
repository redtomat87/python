user_time = int(input("Введите время в секундах >> "))
minute = user_time // 60
hours = minute // 60
ostatokMinut = user_time % 3600
minute_ostatok = ostatokMinut // 60
print(f"{user_time:>02} секунд это {minute:>02} минут или {hours:>02} часов и {minute_ostatok:>02} минут.")
