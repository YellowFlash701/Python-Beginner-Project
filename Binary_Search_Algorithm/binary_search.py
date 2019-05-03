from random import sample


def binary_search(list_, target):
    # Sort the list_ without modifying the original list
    list_ = list_.copy()
    list_.sort()
    left, right = 0, len(list_) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_[middle] < target:
            # Eliminate the left half of the list
            left = middle + 1
        elif list_[middle] > target:
            # Eliminate the right half of the list
            right = middle - 1
        else:
            return True
    return False


if __name__ == "__main__":
    list_len = 10
    rand_list = sample(range(0, 101, 2), list_len)
    try:
        target = int(input('Pick a number between 0-100: '))
        result = binary_search(rand_list, target)
        if result:
            print(f'Found {target} in {rand_list}')
        else:
            print(f'Cannot find {target} in {rand_list}')
    except ValueError:
        print('Please input a valid number')
