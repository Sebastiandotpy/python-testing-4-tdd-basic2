from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end+1)

# function should return the greatest number in a list
def max_num_in_list(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
