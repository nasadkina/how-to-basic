
def power_numbers(numbers):
    return [number ** 2 for number in numbers]

# filter types


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    for i in range(2, number):
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








