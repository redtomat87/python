my_list = [(-1 + 0j), 1, 2.2, True, None, 'string', [3, 4], (5, 6, 6.5), {8: 'eight', 7: 'seven'},
           {9, 10}, frozenset(), range(11), b'twelve', bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]),
           TypeError]

for i, item in enumerate(my_list, 1): #Здесь иы для i берем индекс значения функцией enumerate начиная с 1го номера, а в переменную item пишем значение индекса
    print(f"{i}) {item} - {type(item)}")
