def collatz(number):
    if number % 2 == 0:
        result = int(number // 2)
        print(number // 2)
        return result
    elif number % 2 == 1:
        result = int(3 * number + 1)
        print(3 * number + 1)
        return result
number = input('podaj liczbe')
try:
    while number != 1:
        number = collatz(int(number))
except ValueError:
    print('podana liczba musi byc liczba stala')

