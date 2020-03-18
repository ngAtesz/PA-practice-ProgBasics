def create_numlist():
    count = 0
    numlist = []
    # what is 7?
    for number in range(7):
        count += 1
        numlist.append(count)
    return numlist


def display_content_of_list(numbers, length):
    print('Our list is ' + str(length) + ' long.')
    print('It has the following items: ')
    for number in numbers:
        print(number)


def checking_divisiblity(numbers, length):
    divisible_by_2 = 0
    index = 0
    # There is a typo in the name of iteration variable :)
    for divisibe in range(length):
        if numbers[index]//2 <= 2:
            divisible_by_2 += 1
        index += 1
    print('From the', str(length), 'items, there is ' + str(divisible_by_2) + ' items which are dividible by 2 maximum 2 times')


def main():
    numlist = create_numlist()
    length = len(numlist)
    display_content_of_list(numlist, length)
    checking_divisiblity(numlist, length)


if __name__ == "__main__":
    main()
