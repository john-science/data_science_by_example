# The Fastest Way to Read a CSV File

It is extremely common to need to read CSV files and process them line by line. So it is worth our time to look at the various ways to do this. In this study, we will only look at files under ~200MB. Not because files larger than a GB or even a Terrabyte are uncommon, but because the methods involved in reading files that are too large to fit into memory are different and the results start to depend heavily on how much memory you have.

There is a big parameter space for this problem. To start, we will break our study down into two components: the file read, and the reading method. Obviously, the file size might affect the read time. But what about the number of columns? We will also consider fixed-format files. And we will consider as many different ways to read these files as we can think of.

Obviously, CSV (or fixed-format) files might contain numerical data. But in this instance we are not interested in testing the conversion of strings to float or integers, so we will simply parse the lines into strings. (If you're interested, converting a string to a `float` is much faster than converting it to an `int` in Python.)

## Methods

You can find the Python script I used to run these tests [here]().

#### The File

We will want to test files with various properties:

* **File Type**: simple CSV, fixed format (padded and un-padded)
* **Number of Columns**: 5, 10, 50, 100, 200
* **File Size (MB)**: 1, 5, 10, 50, 100, 200

This means we will need 90 different files to test.

#### Reading Method

There are many, many ways to read a text file in Python. This list is sure to not be exhaustive, but let's try several variations, just to see:

* `for line in f`
* `for line in f.readlines()` (In Python 3.x, or  `f.xreadlines()` in 2.x.)
* `for line in fileinput.input()`
* `pandas.read_csv`
* `pandas.read_fwf`
* `struct` to unpack fwf (see [SO](http://stackoverflow.com/questions/4914008/efficient-way-of-parsing-fixed-width-files-in-python))
* "slicing" fixed-width files (see [SO](http://stackoverflow.com/questions/4914008/efficient-way-of-parsing-fixed-width-files-in-python))

Each of the above approaches will required lots of testing and variations to try and improve performance. I will try to keep as many of these around as possible for the final analysis. Though I expect I will find several dead ends.

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

You can find the iPython script I used to analyze the results and make plots [here]().

> TODO
