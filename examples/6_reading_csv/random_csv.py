
from numpy import array, random
import os
import sys
if sys.version_info[0] < 3:
    range = xrange


def main():
    rand = RandomCsv()
    file_path = rand.generate_csv(1, 8)
    file_path = rand.generate_csv(5, 12)


class RandomCsv(object):

    CHARS = list('pack my box with five dozen liquors PACK MY BOX WITH FIVE DOZEN LIQUORS')

    def __init__(self):
        self.out_dir = 'temp/'
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

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

        return file_path

    @staticmethod
    def generate_string(how_many, str_length=10):
        return [''.join(list(random.choice(RandomCsv.CHARS, str_length))) for _ in range(how_many)]


if __name__ == '__main__':
    main()
