
import sys
if sys.version_info[0] < 3:  range = xrange
from timeit import timeit
from random_csv import RandomCsv

# CONFIGURATION VALUES
COLUMNS = [5, 10, 50, 100, 200]
FILE_SIZE_MB  = [1, 5, 10, 50, 100, 200]
NUMBER_TRIALS = 1


def main():
    print('file_type,number of columns,file size (MB),time (sec)')
    rand = RandomCsv()

    # CSV-reading functions
    csv_readers = [for_line_in_f_split, for_line_in_f_readlines_split,
                   for_line_in_f_xreadlines_split]

    # test CSV files (generate files, then use all reading functions on all the files)
    for col in COLUMNS:
        for file_size in FILE_SIZE_MB:
            file_path = rand.generate_csv(file_size, col)
            for f in csv_readers:
                wrapped = wrapper(f, file_path)
                time_seconds = timeit(wrapped, number=NUMBER_TRIALS) / NUMBER_TRIALS
                line = ','.join(['csv', str(col), str(file_size), f.__name__, str(time_seconds)])
                print(line)

    # test fixed-width files
    pass


def for_line_in_f_split(file_path):
    ''' Read a CSV file using the most basic (and Pythonic) method.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    f = open(file_path, 'r')
    header = f.readline()
    for line in f:
        line_bits = line.strip().split(',')
    f.close()


def for_line_in_f_readlines_split(file_path):
    ''' Read a CSV file using f.readlines, which is slower in Python 2.x,
        but a faster iterator using Python 3.x.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    f = open(file_path, 'r')
    header = f.readline()
    for line in f.readlines():
        line_bits = line.strip().split(',')
    f.close()


def for_line_in_f_xreadlines_split(file_path):
    ''' Read a CSV file using f.xreadlines, which is a faster iterator
        in Python 2.x, but no longer exists in Python 3.x.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    f = open(file_path, 'r')
    header = f.readline()
    for line in f.xreadlines():
        line_bits = line.strip().split(',')
    f.close()


def wrapper(func, *args, **kwargs):
    ''' Helper function to make using timeit easier
        with functions that take arguments.
    '''
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    main()
