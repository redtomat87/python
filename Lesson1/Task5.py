revenue = int(input("Ввекдите значение выручки"))
costs = int(input("Введите значение издержек"))
profit = revenue - costs
if revenue > costs:
    print("Вы работаете в прибыль")
    print(f"Рентабельность выручки {revenue / costs}")
    quality = int(input("Введите численность сотрудников фирмы"))
    print(f"Прибыль в расчёте на одного сотрудника {profit / quality}")
else:
    print("Вы работаете в убыток")
