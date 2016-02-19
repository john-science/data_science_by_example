
from numpy import array, random
import os
import sys
if sys.version_info[0] < 3: range = xrange


def main():
    rand = RandomCsv()
    rand.generate_csv(1, 3, 2, 4)
    rand.generate_csv(5, 5, 12, 4)
    rand.generate_csv(100, 2, 7, 10)


class RandomCsv(object):

    CHARS = list('abcdefghijklmnopqrstuvwxyz rstlne ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def __init__(self):
        self.out_dir = 'temp/'
        os.mkdir(self.out_dir)

    def generate_fixed_width_equal(self, width, file_size,
                                   num_int_cols, num_float_cols, num_str_cols):
        ''' Generate a random fixed-width text file with a set number of columns full of
            strings, floants, and/or integers. Each column has the same width.
            And design the file so it has close to the desired file size (in MB).
        '''
        file_path = self.out_dir + str(file_size) + 'MB_int' + str(num_int_cols) + '_float' + \
                    str(num_float_cols) + '_str' + str(num_str_cols) + '_fixed_equal.txt'
        rows = 100
        data = []

        # build columns of the correct kinds of data types
        for _ in range(num_str_cols):
            data.append(RandomCsv.generate_string(rows, str_length=random.randint(8, 24)))
        for _ in range(num_float_cols):
            data.append(RandomCsv.generate_floats(rows, order=random.randint(1, 4)))
        for _ in range(num_int_cols):
            data.append(RandomCsv.generate_ints(rows, digits=random.randint(3, 8)))

        # transpose the columns into rows
        data = list(map(list, zip(*data)))

        # convert rows of data into strings
        for i in range(len(data)):
            data[i] = ','.join([str(d)[:width].rjust(width) for d in data[i]]) + '\n'

        # build header
        header = ['s' + str(j)[:width].rjust(width) for j in range(num_str_cols)] + \
                 ['f' + str(j)[:width].rjust(width) for j in range(num_float_cols)] + \
                 ['i' + str(j)[:width].rjust(width) for j in range(num_int_cols)]
        header = ','.join(header) + '\n'

        # determine how many rows to write to the file
        number_rows = int((file_size * 1024 * 1024 - len(header)) / len(data[0]))

        # write the file
        f = open(file_path, 'w')
        f.write(header)
        row = 0
        while row < number_rows:
            f.write(data[row % rows])
            row += 1
        f.close()

    def generate_csv(self, file_size, num_int_cols, num_float_cols, num_str_cols):
        ''' Generate a random CSV file with a set number of columns full of
            strings, floants, and/or integers. And design the file so it has
            close to the desired file size (in MB).
        '''
        file_path = self.out_dir + str(file_size) + 'MB_int' + str(num_int_cols) + '_float' + \
                    str(num_float_cols) + '_str' + str(num_str_cols) + '.csv'
        rows = 100
        data = []

        # build columns of the correct kinds of data types
        for _ in range(num_str_cols):
            data.append(RandomCsv.generate_string(rows, str_length=random.randint(8, 24)))
        for _ in range(num_float_cols):
            data.append(RandomCsv.generate_floats(rows, order=random.randint(1, 4)))
        for _ in range(num_int_cols):
            data.append(RandomCsv.generate_ints(rows, digits=random.randint(3, 8)))

        # transpose the columns into rows
        data = list(map(list, zip(*data)))

        # convert rows of data into strings
        for i in range(len(data)):
            data[i] = ','.join([str(d) for d in data[i]]) + '\n'

        # build header
        header = ['str' + str(j) for j in range(num_str_cols)] + \
                 ['float' + str(j) for j in range(num_float_cols)] + \
                 ['int' + str(j) for j in range(num_int_cols)]
        header = ','.join(header) + '\n'

        # determine how many rows to write to the file
        number_rows = int((file_size * 1024 * 1024 - len(header)) / len(data[0]))

        # write the file
        f = open(file_path, 'w')
        f.write(header)
        row = 0
        while row < number_rows:
            f.write(data[row % rows])
            row += 1
        f.close()

    @staticmethod
    def generate_ints(how_many, digits=3):
        return list(random.randint(0, 10**digits, how_many))

    @staticmethod
    def generate_floats(how_many, order=3):
        return list(random.random(how_many) * 10**order)

    @staticmethod
    def generate_string(how_many, str_length=10):
        return [''.join(list(random.choice(RandomCsv.CHARS, str_length))) for _ in range(how_many)]


if __name__ == '__main__':
    main()
