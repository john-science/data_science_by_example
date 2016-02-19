
from numpy import array, random
import os
import sys
if sys.version_info[0] < 3:  range = xrange


def main():
    rand = RandomCsv()
    rand.generate_csv(1, 8)
    rand.generate_csv(5, 12)
    rand.generate_csv(100, 68)
    rand.generate_fixed_format(1, 6, 10)
    rand.generate_fixed_format(5, 8, 24, padding=1)
    rand.generate_fixed_format(100, 24, 12, padding=3)


class RandomCsv(object):

    CHARS = list('pack my box with five dozen liquors')

    def __init__(self):
        self.out_dir = 'temp/'
        os.mkdir(self.out_dir)

    def generate_fixed_format(self, file_size, columns, width, padding=0):
        ''' Generate a random fixed-width text file with a set number of columns full of
            randomly-generated strings. Design the file so it has close to the desired
            file size (in MB).
            Each column in this fixed-width file will be the same width, as this will obviously
            be easier to parse than a variable-width file.
        '''
        file_path = self.out_dir + str(file_size) + 'MB_' + str(columns) + '_columns' + \
                    str(padding) + 'padding.txt'
        pad = ' '*padding
        rows = 100
        data = []

        # build columns of random strings
        for _ in range(columns):
            data.append(RandomCsv.generate_string(rows, str_length=width))

        # transpose the columns into rows
        data = list(map(list, zip(*data)))

        # convert rows of data into strings
        for i in range(len(data)):
            data[i] = pad.join([str(d) for d in data[i]]) + '\n'

        # build header
        header = [('c' + str(j))[:width].rjust(width) for j in range(columns)]
        header = pad.join(header) + '\n'

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

    def generate_csv(self, file_size, columns):
        ''' Generate a random CSV file with a set number of columns full of
            strings, floants, and/or integers. And design the file so it has
            close to the desired file size (in MB).
        '''
        file_path = self.out_dir + str(file_size) + 'MB_int' + str(columns) + '_columns.csv'
        rows = 100
        data = []

        # build columns of strings
        for _ in range(columns):
            data.append(RandomCsv.generate_string(rows, str_length=random.randint(8, 24)))

        # transpose the columns into rows
        data = list(map(list, zip(*data)))

        # convert rows of data into strings
        for i in range(len(data)):
            data[i] = ','.join([str(d) for d in data[i]]) + '\n'

        # build header
        header = ['col' + str(j) for j in range(columns)]
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
    def generate_string(how_many, str_length=10):
        return [''.join(list(random.choice(RandomCsv.CHARS, str_length))) for _ in range(how_many)]


if __name__ == '__main__':
    main()
