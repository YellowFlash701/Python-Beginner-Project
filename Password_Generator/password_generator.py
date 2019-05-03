from random import choice
from string import ascii_letters, digits, punctuation

CHAR = {
    'letter': [x for x in ascii_letters],
    'digit': [x for x in digits],
    'symbol': [x for x in punctuation]
}


# Get value from the user
def get_val(val):
    user_input = input(f'How many {val} you want? (X: Cancel): ')
    return int(user_input) if user_input.lower() != 'x' else None


def generate(length, **kwargs):
    """
    Generate a random password by the given length.

    The user can provide optional arguments (letter, digit, and symbol) to
    determine how many each of the characters will appear in the password. If
    the sum of all optional arguments is lower than the length provided by the
    user, the sum of them will override the password length. Raise ValueError
    if the sum of two or more optional arguments exceeds the password length.
    """
    kw = ('letter', 'digit', 'symbol')
    kw_sum = kw_count = 0
    for k in kw:
        # Assign None to kwargs[k] if k is not in kwargs otherwise increment
        # kw_sum by keyword argument value and kw_count by 1
        kw_val = kwargs.setdefault(k, None)
        if kw_val is not None:
            # Make sure kw_val is not a negative number
            kw_val = kw_val if kw_val >= 0 else 0
            kw_sum += kw_val
            kw_count += 1
    # Sum of two or more keyword arguments exceeds the length
    if kw_count >= 2 and kw_sum > length:
        raise ValueError('sum of keyword arguments exceeds length')
    # Sum of all keyword arguments is lower than the length
    if kw_count == 3 and kw_sum < length:
        # Override length with the sum of keyword arguments
        length = kw_sum
    # Create a list of keywords provided by the user (unless the keyword
    # argument value is None or lower than one)
    kw_list = [x for x in kwargs if kwargs[x] is not None and kwargs[x] > 0]
    # Create a list of keywords with None (default value for keyword
    # arguments) as their value
    default_list = [x for x in kwargs if kwargs[x] is None]
    # Create a list to store all the password characters
    password = [None] * length
    # Create a list of all index with empty (None) value in the password list
    none_index = list(range(length))
    if kw_list:
        empty = False
    for _ in range(length):
        if not kw_list:
            empty = True
            kw_list = default_list
        rand_kw = choice(kw_list)
        rand_index = choice(none_index)
        # Assign a random character to password list at a random index
        password[rand_index] = choice(CHAR[rand_kw])
        none_index.remove(rand_index)
        # If kw_list is not empty and kwargs[rand_kw] value is not None, reduce
        # the value by 1
        if not empty and kwargs[rand_kw] is not None:
            kwargs[rand_kw] -= 1
            # If kwargs[rand_kw] value fall below 1, assign None to
            # kwargs[rand_kw] and remove the rand_kw from kw_list
            if kwargs[rand_kw] < 1:
                kwargs[rand_kw] = None
                kw_list.remove(rand_kw)
    return ''.join(password)


def main():
    min_len, max_len = 6, 20
    letter = digit = None
    print('+---------Password Generator---------+\n')
    try:
        length = int(
            input(f'Enter the password length ({min_len}-{max_len}): '))
        # Make sure the length is not lower than minimum length
        if length < min_len:
            length = min_len
        # Make sure the length is not higher than maximum length
        elif length > max_len:
            length = max_len
        add_input = input('Input additional options? (Y/N): ')
        if add_input.lower() == 'y':
            letter = get_val('letter')
            if letter is None or letter < length:
                digit = get_val('digit')
    except ValueError:
        print('Invalid input!')
    else:
        password = generate(length, letter=letter, digit=digit)
        print(f'\nYour password: {password}')


if __name__ == "__main__":
    main()
