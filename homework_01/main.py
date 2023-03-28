import math


def power_numbers(*numbers):
    return [number ** 2 for number in numbers]


# filter types
#numbers = [1, 2, 3, 4]
#print(power_numbers(numbers))

ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True



def filter_numbers(numbers_list, filter_type):
    if filter_type == ODD:
        return [number for number in numbers_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in numbers_list if number % 2 == 0]
    if filter_type == PRIME:
        return [number for number in numbers_list if (is_prime(number) is True)]
