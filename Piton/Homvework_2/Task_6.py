s = input('Введите строку по кайфу снова')
print(f"Кол-во гласных в строке: {sum([1 for x in s if x in 'АЕЁИОУЫЭЮЯ' or x in 'аеёиоуыэюя}'])}")