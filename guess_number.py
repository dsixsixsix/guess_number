from random import randint

number = randint(1, 100)

print(f'Угайдай число от 1 до 100.')

while True:
    guess = int(input('Введите число: '))

    if guess > number:
        print(f'Загаданное число меньше.')
    if guess < number:
        print(f'Загаданное число больше.')
    if guess == number:
        break

print(f'Вы угадали число!')