import random as r
from time import sleep


def generate_numbers_with_printing():
    list_of_numbers = []
    num_frequency = 9
    for number in range(num_frequency):
        list_of_numbers.append(r.randint(1, 20))
        print(list_of_numbers)
        sleep(0.1)
    return list_of_numbers


def generate_numbers_without_printing():
    list_of_numbers = []
    for number in range(9):
        list_of_numbers.append(r.randint(1, 20))
    return list_of_numbers


def ascending_nums(numbers):
    num_frequency = 9
    for i in range(num_frequency):
        print(numbers[:num_frequency])
        num_frequency = num_frequency - 1
        sleep(0.1)


def main():
    program_frequency = 2
    for i in range(program_frequency):
        generate_numbers_with_printing()
        numlist = generate_numbers_without_printing()
        ascending_nums(numlist)


if __name__ == "__main__":
    main()
