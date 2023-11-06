n = int(input('Введите число, чтобы проверить его на простоту'))
k = 0
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        k += 1
        print(f'Число {n} не простое')
        break
if k == 0:
    print(f'Число {n} простое')