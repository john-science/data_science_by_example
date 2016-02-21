
from csv import reader, DictReader
import fileinput
from mmap import mmap, PROT_READ
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
NUMBER_TRIALS = 1


def main():
    print('\nfile_type,number of columns,file size (MB),function,time (sec)')
    rand = RandomCsv()

    # CSV-reading functions
    csv_readers = [for_line_in_f_split, for_line_in_f_split_with, pandas_read_csv_df,
                   fileinput_with_firstline, csv_reader, csv_dict_reader, mmap_while, mmap_for]
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
            #break
        #break

    print('')


'''
More to come!

http://softwarerecs.stackexchange.com/questions/7463/fastest-python-library-to-read-a-csv-file
'''

def wrapper(func, *args, **kwargs):
    ''' Helper function to make using timeit easier
        with functions that take arguments.
    '''
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


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
    ''' I'm not sure this function is as good as the rest, as it reads the data
        into a giant Pandas Data Frame and means you have to change whatever
        line-by-line reading logic you were going to use.
    '''
    df = read_csv(file_path)


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


def open_with_numpy_loadtxt(file_path):
    '''
    http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting
    '''
    data = loadtxt(open(file_path, 'rb'), delimiter=',', skiprows=1)
    return data


if __name__ == '__main__':
    main()
