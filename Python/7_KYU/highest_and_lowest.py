def high_and_low(numbers):
    numbers_list = [int(num) for num in numbers.split()]
    sorted_string = sorted(numbers_list)
    result = '{} {}'.format(sorted_string[-1], sorted_string[0])
    return result

assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9", 'Failed test 1'
assert high_and_low("322 -765 -842 159 844 -946 -336 809 -984 563 772 151 504 -301 -605") == "844 -984", 'Failed test 2'
assert high_and_low("1 2 3") == "3 1", 'Failed test 3'

print('All tests passed')
