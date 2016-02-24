
from csv import reader, DictReader
import fileinput
from mmap import mmap, PROT_READ
from numpy import fromfile, genfromtxt, loadtxt, nditer
from pandas import read_csv
import re
import sys
if sys.version_info[0] < 3:
    range = xrange
from timeit import timeit
from random_csv import RandomCsv

# CONFIGURATION VALUES
COLUMNS = [5, 10, 50, 100, 200]
FILE_SIZE_MB  = [1, 5, 10, 50, 100, 200]
NUMBER_TRIALS = 10


def main():
    print('function,file size (MB),number of columns,time (sec)')
    rand = RandomCsv()

    # CSV-reading functions
    csv_readers = [simple_read, naive_read_split_split,
                   for_line_in_f_split, for_line_in_f_split_with, pandas_read_csv_df,
                   pandas_read_csv_iterrows, fileinput_with_firstline, csv_reader,
                   csv_dict_reader, mmap_while, mmap_for, numpy_loadtxt, numpy_genfromtxt,
                   numpy_genfromtxt_nditer, numpy_genfromtxt_range_shape]
    if sys.version_info[0] < 3:
        csv_readers.append(for_line_in_f_xreadlines_split)
        csv_readers.append(re_xreadlines)
    else:
        csv_readers.append(for_line_in_f_readlines_split)
        csv_readers.append(for_line_in_f_readlines_split_with)
        csv_readers.append(re_readlines)
        csv_readers.append(re_readlines_with)

    # test CSV files (generate files, then try all reading functions on all the files)
    for col in COLUMNS:
        for file_size in FILE_SIZE_MB:
            file_path = rand.generate_csv(file_size, col)
            for f in csv_readers:
                wrapped = wrapper(f, file_path)
                time_seconds = timeit(wrapped, number=NUMBER_TRIALS) / NUMBER_TRIALS
                line = ','.join([f.__name__, str(file_size), str(col), str(time_seconds)])
                print(line)


def wrapper(func, *args, **kwargs):
    ''' Helper function to make using timeit easier
        with functions that take arguments.
    '''
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def simple_read(file_path):
    ''' This simply reads the entire file into one long string.
        Obviously, this does not parse a CSV in a line-by-line
        fashion, this is just meant to be a baseline to compare
        the reading functions against.
    '''
    whole_file = open(file_path, 'r').read()


def naive_read_split_split(file_path):
    ''' This is the most naive way to parse a CSV file line-by-line.
        Read the whole file into one big string, then split on
        carriage returns and split on commas.
        One hopes that every other CSV parsing approach will be
        significantly faster than this, or what's the point?
    '''
    lines = open(file_path, 'r').read().split('\n')
    header = lines.pop(0)
    line_bits = None
    for line in lines:
        line_bits = line.split(',')


def for_line_in_f_split(file_path):
    ''' Read a CSV file using the most basic (and Pythonic) method.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    f = open(file_path, 'r')
    header = f.readline()
    for line in f:
        line_bits = line.rstrip().split(',')
    f.close()


def for_line_in_f_split_with(file_path):
    ''' Read a CSV file using the most basic (and Pythonic) method.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    with open(file_path, 'r') as f:
        header = f.readline()
        for line in f:
            line_bits = line.rstrip().split(',')


def for_line_in_f_readlines_split(file_path):
    ''' Read a CSV file using f.readlines, which is slower in Python 2.x,
        but a faster iterator using Python 3.x.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    f = open(file_path, 'r')
    header = f.readline()
    for line in f.readlines():
        line_bits = line.rstrip().split(',')
    f.close()


def for_line_in_f_readlines_split_with(file_path):
    ''' Read a CSV file using f.readlines, which is slower in Python 2.x,
        but a faster iterator using Python 3.x.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    with open(file_path, 'r') as f:
        header = f.readline()
        for line in f.readlines():
            line_bits = line.rstrip().split(',')


def for_line_in_f_xreadlines_split(file_path):
    ''' Read a CSV file using f.xreadlines, which is a faster iterator
        in Python 2.x, but no longer exists in Python 3.x.
        And then use `split` to break the line up into columns of data.
    '''
    line_bits = None
    f = open(file_path, 'r')
    header = f.readline()
    for line in f.xreadlines():
        line_bits = line.rstrip().split(',')
    f.close()


def pandas_read_csv_df(file_path):
    ''' Using the pandas read_csv function is fast, but doesn't allow
        line-by-line reading. So I think this seems artificially faster
        than it should be.
    '''
    df = read_csv(file_path)


def pandas_read_csv_iterrows(file_path):
    ''' Using the pandas read_csv function is fast, but doesn't allow
        line-by-line reading. So I think this seems artificially faster
        than it should be.
    '''
    df = read_csv(file_path)
    line_bits = None
    for i, row in df.iterrows():
        line_bits = row


def re_readlines(file_path):
    ''' Using the Python standard library `re` to use regular expressions
        instead of `string.split()`.
        In this version I use the Python v3.x `f.readlines()` to read the file.
    '''
    line_bits = None
    f = open(file_path, 'r')
    for line in f.readlines():
        line_bits = re.split(',', line.rstrip())
    f.close()


def re_readlines_with(file_path):
    ''' Using the Python standard library `re` to use regular expressions
        instead of `string.split()`.
        In this version I use the Python v3.x `f.readlines()` to read the file.
        I also try the "with open" syntax.
    '''
    line_bits = None
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line_bits = re.split(',', line.rstrip())


def re_xreadlines(file_path):
    ''' Using the Python standard library `re` to use regular expressions
        instead of `string.split()`.
        In this version I use the Python v2.x `f.xreadlines()` to read the file.
    '''
    line_bits = None
    with open(file_path, 'r') as f:
        for line in f.xreadlines():
            line_bits = re.split(',', line.rstrip())


def fileinput_with_firstline(file_path):
    ''' Using the Python standard library `fileinput` to read a CSV file.
        I still need to use split to break the string into a list.
    '''
    line_bits = None
    for line in fileinput.input(file_path):
        if fileinput.isfirstline():
            header = line
        line_bits = line.rstrip().split(',')


def csv_reader(file_path):
    ''' Using the Python standard `csv` library to read a CSV file.
        Each non-header row will pop out as a list of strings.
    '''
    line_bits = None
    with open(file_path, 'r') as csvfile:
        r = reader(csvfile, delimiter=',')
        for row in r:
            line_bits = row


def csv_dict_reader(file_path):
    ''' Using the Python standard `csv` library to read a CSV file.
        This time I am parsing the entire file so that each row
        is a dictionary where the row headers are the keys.
    '''
    line_bits = None
    with open(file_path, 'r') as csvfile:
        reader = DictReader(csvfile, delimiter=',')
        for row in reader:
            line_bits = row


def mmap_while(file_path):
    ''' Using the Python standard `mmap` library to read a CSV file,
        still requires using the `split` string method.
    '''
    line_bits = None
    with open(file_path, "r+b") as f:
        m = mmap(f.fileno(), 0, prot=PROT_READ)
        header = m.readline()
        while True:
            line = m.readline()
            if line == b'':
                break
            line_bits = str(line).rstrip().split(',')


def mmap_for(file_path):
    ''' Using the Python standard `mmap` library to read a CSV file,
        still requires using the `split` string method.
    '''
    line_bits = None
    with open(file_path, "r+b") as f:
        m = mmap(f.fileno(), 0, prot=PROT_READ)
        header = m.readline()
        for line in iter(m.readline, ""):
            if line == b'':
                break
            line_bits = str(line).rstrip().split(',')


def numpy_loadtxt(file_path):
    '''
    Read the simple CSV file using the numpy.loadtxt module.
    NOTE: This function returns each line as a list of bytes, not strings.
          So, to be fair, I should convert these to lists of strings, but
          it is already so slow I know `loadtxt` isn't worth it.
    '''
    array_2d_strs = loadtxt(open(file_path, 'r'), delimiter=',', skiprows=1, dtype='str')


def numpy_fromfile(file_path):
    '''
    Read the simple CSV file using the numpy.fromfile module.
    '''
    # TODO: This doesn't work at all: Segmentation fault (core dumped)
    all_lines = fromfile(file_path, dtype='str', sep=',', count=-1)


def numpy_genfromtxt(file_path):
    '''
    Read the simple CSV file using the numpy.genfromtxt module.
    '''
    array_2d_strs = genfromtxt(file_path, dtype='str', delimiter=',', skip_header=1)


def numpy_genfromtxt_nditer(file_path):
    '''
    Read the simple CSV file using the numpy.genfromtxt module.
    '''
    array_2d_strs = genfromtxt(file_path, dtype='str', delimiter=',', skip_header=1)
    line_bits = None
    for line in nditer(array_2d_strs):
        line_bits = line


def numpy_genfromtxt_range_shape(file_path):
    '''
    Read the simple CSV file using the numpy.genfromtxt module.
    '''
    array_2d_strs = genfromtxt(file_path, dtype='str', delimiter=',', skip_header=1)
    line_bits = None
    rows,colums = array_2d_strs.shape
    for i in range(rows):
        line_bits = array_2d_strs[i]


if __name__ == '__main__':
    main()
