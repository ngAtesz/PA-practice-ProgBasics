def create_numlist(limit):
    numlist = []
    for number in range(1, limit+1):
        numlist.append(number)
    return numlist


def display_content_of_list(numbers):
    print('Our list is ' + str(len(numbers)) + ' long.')
    print('It has the following items: ')
    for number in numbers:
        print(number)


def count_divisibles_by_two(numbers):
    divisible_by_2 = 0
    for number in numbers:
        if number // 2 <= 2:
            divisible_by_2 += 1
    
    return divisible_by_2


def main():
    count = 7
    numlist = create_numlist(count)
    display_content_of_list(numlist)
    divisible_count = count_divisibles_by_two(numlist)
    print('From the', str(len(numlist)), 'items, there is ' + str(divisible_count) + ' items which are dividible by 2 maximum 2 times')


if __name__ == "__main__":
    main()
