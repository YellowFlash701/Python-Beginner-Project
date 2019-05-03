from random import randint

num_range = 0, 20
secret_num = randint(*num_range)

while True:
    try:
        user_num = int(
            input(f'Guess a number between {num_range[0]}-{num_range[1]}: '))
        if user_num > secret_num:
            print('Too high...')
        elif user_num < secret_num:
            print('Too low...')
        else:
            print('Hit!')
            break
    except ValueError:
        print('Please input a valid number!')
    print()
