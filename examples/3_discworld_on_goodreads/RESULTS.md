# Parsing Goodreads for Information on Discworld

In case you aren't already familiar with it, [goodreads](https://www.goodreads.com/) does for books what [IMDB](https://www.imdb.com/) does for movies. It's a great site, with a lot of information to dig through.

This is a basic example of website parsing to get your data. To make it interesting, I choose the Discworld series of books. It is one of the longest series of books ever written, with over 40 books written over 30 years. This also gives us the opportunity to try out data plotting.

## Method

The first step for this project, was to get the HTML for the `goodreads` page. I originally did this with a simple [requests]() pull:

    requests.get('https://www.goodreads.com/series/40650-discworld')

But, the `goodreads` site is free to reformat their webpages. So just in case, I have cached the result [here](goodreads_discworld.html).

However you get the HTML for that webpage, the next steps are the same:

* Use [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) to parse the HTML as XML and get a set of data for each book: title, number of user ratings, average rating, publication year, number in series, and if it's part of a sub-series.
* Load the book data into [pandas](http://pandas.pydata.org/) for analysis.
* Use `pandas` to find the top ten books by average user rating and number of user ratings.
* Use the `pandas` `groupby` method to determine which books in the series are part of a smaller sub-series of stories.
* Use the `pandas` `groupby` method to determine which sub-series are most popular.
* Use `pandas` to display a list of the books in the most popular three sub-series.

## Results

TODO
