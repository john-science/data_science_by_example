
from numpy import array, random


CHARS = list('abcdefghijklmnopqrstuvwxyz rstlne ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def main():
    pass



def generate_csv(file_path, file_size, num_str_cols, num_float_cols, num_int_cols):
    ''' Generate a random CSV file with a set number of columns full of
        strings, floants, and/or integers. And design the file so it has
        close to the desired file size (in MB).
    '''
    rows = 100
    data = []

    # build columns of the correct kinds of data types
    for _ in xrange(num_str_cols):
        data.append(generate_string(rows, str_length=random.randint(8, 24))
    for _ in xrange(num_float_cols):
        data.append(generate_floats(rows, order=random.randint(1, 4)))
    for _ in xrange(num_int_cols):
        data.append(generate_ints(rows, order=random.randint(3, 8)))

    # transpose the columns into rows
    data = map(list, zip(*data))

    # convert rows of data into strings
    for i in xrange(len(data)):
        data[i] = ','.join([str(d) for d in data[i]]) + '\n'

    # build header
    header = ['str' + str(j) for j in xrange(num_str_cols)] + \
             ['float' + str(j) for j in xrange(num_float_cols)] + \
             ['int' + str(j) for j in xrange(num_int_cols)]
    header = ','.join(header) + '\n'

    # determine how many rows to write to the file
    number_rows = int(((file_size * 1024 * 1024) - len(header)) / len(data[0]))

    # write the file
    f = open(file_path, 'w')
    f.write(header)
    row = 0
    while r < xrange(number_rows):
        f.write(data[row % rows))

    f.close()


def generate_ints(how_many, digits=3):
    return list(random.randint(0, 10**digits, how_many))


def generate_floats(how_many, order=3):
    return list(random.random(how_many) * 10**order)


def generate_string(how_many, str_length=10):
    return [''.join(list(random.choice(CHARS, str_length))) for _ in xrange(how_many)]


if __name__ == '__main__':
    main()
