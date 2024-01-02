import re
import sys

numbers = ['one', 'two', 'three', 
           'four', 'five', 'six', 
           'seven', 'eight', 'nine']

NUMBER_RE = re.compile(
    r'[1-9]|' + '|'.join(numbers),
    re.IGNORECASE | re.DOTALL,
)

number_dict = dict(zip(numbers, range(1, 10)))


def map_number(num):
    if num.isdigit():
        return int(num)
    return number_dict.get(num, None)


def get_number(line):
    '''
    Finds the first and the last digit in a line of text
    and return the number of their concatenation.
    '''
    numbers = [num for m in NUMBER_RE.findall(line) if (num := map_number(m))]
    print(numbers)
    return int(f"{numbers[0]}{numbers[-1]}")


def read_sum(filename):
    '''
    Opens the file <filename> and computes the sum of the numbers 
    represented by the first and the last digit of each line.
    '''
    with open(filename, 'r') as f:
        return sum(get_number(line) for line in f.readlines())


if __name__ == '__main__':
    match len(sys.argv):
        case 2:
            filename = sys.argv[1]
        case 1:
            try:
                filename = input('Enter name of input file: ')
            except KeyboardInterrupt:
                sys.exit(1)
        case _:
            print('Too many arguments - Expected (1): <inputfile>')
            sys.exit(-1)

    print(read_sum(filename))
