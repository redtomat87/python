"""a = int(input("Введите результат спортсмена в первый день :"))
b = int(input("Финальная дистанция спортсмена :"))
n = 1
while a < b:
    a = a * 1.1
    n += 1
print(f"Через {n} дней спортсмен пробежит {b} километров")"""


start = float(input("Введите результат за 1 день:"))
finish = float(input("Введите цель спортсмена:"))
days = 1
km = start
while km < finish:
    start = start + 0.1 * start
    days += 1
    km = km + start
print(f"Вы достигнете финиша через", days)
