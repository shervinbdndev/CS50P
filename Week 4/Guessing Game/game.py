import random

while True:
    try:
        level = int(input('Level: '))
    except ValueError:
        continue
    if (level <= 0):
        continue

    num = random.randint(1 , level)
    break


while True:
    try:
        guess = int(input('Guess: '))
        if (guess <= 0):
            continue
    except ValueError:
        continue
    if (guess < num):
        print('Too small!')
    elif (guess > num):
        print('Too large!')
    else:
        print('Just right!')
        break