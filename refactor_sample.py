import random as r
from time import sleep


def print_numlist(number_list, backwards=False):
    upper_limit = len(number_list)
    for index in range(len(number_list)):
        if backwards:
            print(number_list[:upper_limit])
            upper_limit = upper_limit - 1
        else:
            print(number_list[:index+1])
        sleep(0.1)


def generate_numbers(count):
    list_of_numbers = []
    for _ in range(count):
        list_of_numbers.append(r.randint(1, 20))
    return list_of_numbers


def main():
    program_frequency = 2
    for _ in range(program_frequency):
        nums = generate_numbers(9)
        print_numlist(nums)
        numlist = generate_numbers(9)
        print_numlist(numlist, True)


if __name__ == "__main__":
    main()
