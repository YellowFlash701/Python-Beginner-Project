from random import choice

rps = ('rock', 'paper', 'scissors')
rps_dict = {
    'rock': {'strong': 'scissors', 'weak': 'paper'},
    'paper': {'strong': 'rock', 'weak': 'scissors'},
    'scissors': {'strong': 'paper', 'weak': 'rock'}
}


def print_result(user_score, com_score, win, lose, tie):
    print('Result:', end=' ')
    if user_score > com_score:
        print('You win!')
    elif user_score < com_score:
        print('You lose...')
    else:
        print('Draw.')
    print('--------------------')
    # Print scores
    print(f'Your score: {user_score}')
    print(f'Computer score: {com_score}')
    print('--------------------')
    # Print statistics
    print(f'Win: {win}')
    print(f'Lose: {lose}')
    print(f'Tie: {tie}')


def play(rounds):
    game_result = {
        'user_score': 0,
        'com_score': 0,
        'win': 0,
        'lose': 0, 
        'tie': 0
    }
    while rounds > 0:
        user_input = input(
            'Enter your choice (1: Rock, 2: Paper, 3: Scissors, 0: Quit): ')
        # Check whether the input is in the options
        if user_input in ('1', '2', '3'):
            rounds -= 1
            user_hand = rps[int(user_input) - 1]
            com_hand = choice(rps)
            # user_hand is strong against com_hand
            if rps_dict[user_hand]['strong'] == com_hand:
                game_result['user_score'] += 1
                game_result['win'] += 1
                result = 'You win!'
            # user_hand is weak against com_hand
            elif rps_dict[user_hand]['weak'] == com_hand:
                game_result['com_score'] += 1
                game_result['lose'] += 1
                result = 'You lose...'
            # Tie
            else:
                game_result['tie'] += 1
                result = 'Tie.'
            print(
                f'You -> {user_hand}. Computer -> {com_hand}. {result}')
        elif user_input == '0':
            break
        else:
            print('Invalid input!')
        print()
    print_result(**game_result)


if __name__ == "__main__":
    print('Welcome to Rock-Paper-Scissors Game!')
    try:
        rounds = int(input('How many rounds you want to play? '))
        play(rounds)
    except ValueError:
        print('Please input a valid number!')
