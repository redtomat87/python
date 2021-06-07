my_string = input("Введите строку из нескольких слов, разделённых пробелами: ").split()

for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')