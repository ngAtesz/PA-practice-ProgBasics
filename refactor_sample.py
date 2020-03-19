import random as r
from time import sleep


def print_numbers(number_list):
    for index in range(len(number_list)):
        print(number_list[:index+1])
        sleep(0.1)



def generate_numbers(count):
    list_of_numbers = []
    for _ in range(count):
        list_of_numbers.append(r.randint(1, 20))
    return list_of_numbers


def print_numbers_backwards(numbers):
    upper_limit = len(numbers)
    for i in range(upper_limit):
        print(numbers[:upper_limit])
        upper_limit = upper_limit - 1
        sleep(0.1)


def main():
    program_frequency = 2
    for i in range(program_frequency):
        nums = generate_numbers(9)
        print_numbers(nums)
        numlist = generate_numbers(9)
        print_numbers_backwards(numlist)


if __name__ == "__main__":
    main()
