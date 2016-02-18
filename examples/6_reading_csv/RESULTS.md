# The Fastest Way to Read a CSV File

In the science and data science worlds it is extremely common to need to read CSV files, and process them line by line. So it is worth our time to look at the various ways to do this. In this study, we will only look at files under ~200MB. Not because files larger than a GB or even a Terrabyte are uncommon, but because the methods involved in reading files that are too large to fit into memory are different and the results start to depend heavily on how much memory you will have.

There is a big parameter space for this problem. To start, we will break our study down into two components: the file being read, and the method used to read it. Obviously the file size might affect the read time. But we will also consider: the number of columns, the data types of the text in each column, and we should consider fixed-width file types. And we will consider as many different was to read the files as we can think of.

## Methods

You can find the Python script I used to run these tests [here]().

#### The File

We will want to test files with various properties:

* **File Type**: simple CSV, fixed format (with equal or variable widths)
* **Data Types**: just floats, floats and ints, numbers and strings, or just strings
* **Number of Columns**: 5, 10, 50, 100, 200
* **File Size (MB)**: 1, 5, 10, 50, 100, 200

This gives us a grand total of 360 different files to test.

#### Reading Method

There are many, many ways to read a text file in Python. This list is sure to not be exhaustive, but let's try several variations, just to see:

* `for line in f`
* `for line in f.readlines()` (For completeness, this is a Python 2.7-only option.)
* `for line in f.xreadlines()` (In Python 3.x, this is simply `f.readlines()`)
* `for line in fileinput.input()`
* `pandas.read_csv`

This may only look like 5 different methods to reading a file. But we will want to try variations on most of these. For instance, we may want to try different ways of reading fixed-width files, as that has not been a high-priority target for a lot of Python developers lately.

#### How to Time the Test

To time our various trials we will use the [timeit](https://docs.python.org/2/library/timeit.html) module. Here is a toy example:

    >>> def costly_func(lst):
    ...     return map(lambda x: x^2, lst)
    ... 
    >>> 
    >>> def wrapper(func, *args, **kwargs):
    ...     def wrapped():
    ...         return func(*args, **kwargs)
    ...     return wrapped
    ... 
    >>> short_list = range(10) 
    >>> wrapped = wrapper(costly_func, short_list)
    >>> timeit.timeit(wrapped, number=1000)
    0.00409102439880371

The results would be more accurate with a higher `number` of iterations. But I think there's a good chance that reading some of these files will take on the order of a second, so we can't run a million iterations.

## RESULTS

TODO
