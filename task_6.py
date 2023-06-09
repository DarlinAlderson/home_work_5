# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

print('Task number 6')
from random import randint


def guess_the_num(number, attempt):
    if attempt == 0:
        return 'Вы не угадали :( Попробуйте еще раз!'

    print(f'Отгадайте число, у вас есть {attempt} попыток.')
    a = int(input('Число: '))

    if a == number:
        return f'Вы угадали! Попыток осталось: {attempt - 1}'
    elif a > number:
        print('Ваше число больше загаданного!')
    else:
        print('Ваше число меньше загаданного!')

    return guess_the_num(number, attempt - 1)


num = randint(0, 100)
print(guess_the_num(num, 10))
