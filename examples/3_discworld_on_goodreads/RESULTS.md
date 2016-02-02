# Parsing Goodreads for Information on Discworld

In case you aren't already familiar with it, [goodreads](https://www.goodreads.com/) does for books what [IMDB](https://www.imdb.com/) does for movies. It's a great site, with a lot of information to dig through.

This is a basic example of website parsing to get your data. To make it interesting, I choose the Discworld series of books. It is one of the longest series of books ever written, with over 40 books written over 30 years. This also gives us the opportunity to try out data plotting.

## Method

The first step for this project, was to get the HTML for the `goodreads` page. I originally did this with a simple [requests]() pull:

    requests.get('https://www.goodreads.com/series/40650-discworld')

But, the `goodreads` site is free to reformat their webpages. So just in case, I have cached the result here:

    TODO

## Results

TODO
