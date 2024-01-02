import sys


def get_number(line):
    '''
    Finds the first and the last digit in a line of text
    and return the number of their concatenation.
    '''
    numbers = [ch for ch in line if ch.isdigit()]
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
