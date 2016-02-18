# The Fastest Way to Read a CSV File

What's the fastest way to read in large or large-ish CSV files? Does it depend on the data type in the columns? Should you use a pre-canned tool (like in `pandas`), or build your own? Is it faster to read CSV files or fixed-width files? What can you do to speed things up? This is a big question, but it makes a big difference. So let's test.

## Methods

You can find the Python script I used to run these tests [here]().

First, we will break our study down into two components: the file being read, and the method for reading the file.

#### The File

We will want to test files with various properties:

* **File Type**: simple CSV, or fixed format (with fixed or variable widths)
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

With 5 different reading methods, our work is cut out for us with 1800 different tests to run.

#### How to Time the Test

TODO

## RESULTS

TODO
