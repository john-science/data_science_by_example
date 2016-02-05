# Parsing Goodreads for Information on Discworld

In case you aren't familiar with it, [goodreads](https://www.goodreads.com/) does for books what [IMDB](https://www.imdb.com/) does for movies. It's a great site, with a lot of information to dig through.

This is a basic example of parsing a website parsing for data. To make it interesting, I choose the Discworld series of books. It is one of the longest series of books ever written, with 41 primary books written over 32 years.

## Method

The first step was to get the HTML from the relevant `goodreads` page. I originally did this with a simple [requests](http://docs.python-requests.org/en/latest/) pull:

    requests.get('https://www.goodreads.com/series/40650-discworld')

Just in case the `goodreads` site reformats their webpages, I have cached the result [here](goodreads_discworld.html).

After getting the HTML:

* Use [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) to parse the HTML and get a collection of data for each book: title, number of user ratings, average rating, publication year, number in series, and if it's part of a sub-series.
* Load the book data into [pandas](http://pandas.pydata.org/) for analysis.
* Use `pandas` to find the top ten books by average user rating and number of user ratings.
* Use the `pandas` `groupby` method to determine which books in the series are part of a smaller sub-series of stories.
* Use the `pandas` `groupby` method to determine which sub-series are most popular.
* Use `pandas` to display a list of the books in the most popular three sub-series.

The analysis here is abbreviated, as the goal of this example is to try using `requests` along with `beautifulsoup` to parse a webpage.

## Results

First off, there are 41 books in the Discworld series. Naively, you might just start with the two-book mini-series that started it all:

* [The Colour of Magic](https://www.goodreads.com/book/show/34497.The_Color_of_Magic)
* [The Light Fantastic](https://www.goodreads.com/book/show/34506.The_Light_Fantastic)

But the series doesn't need to be read in order. So these four books appear in both the top-ten lists for highest-rated and most-read books in the series:

* [Night Watch](https://www.goodreads.com/book/show/47989.Night_Watch)
* [Going Postal](https://www.goodreads.com/book/show/64222.Going_Postal)
* [Guards! Guards!](https://www.goodreads.com/book/show/64216.Guards_Guards_)
* [Small Gods](https://www.goodreads.com/book/show/34484.Small_Gods)

Another option is to pick one of the sub-series of books inside the main series. Here are the books in the most popular three sub-series:

title | subseries
:--- | :---
[Guards! Guards!](https://www.goodreads.com/book/show/64216.Guards_Guards_) | City Watch
[Men at Arms](https://www.goodreads.com/book/show/400354.Men_at_Arms) | City Watch
[Feet of Clay](https://www.goodreads.com/book/show/34527.Feet_of_Clay) | City Watch
[Jingo](https://www.goodreads.com/book/show/47990.Jingo) | City Watch
[The Fifth Elephant](https://www.goodreads.com/book/show/63720.The_Fifth_Elephant) | City Watch
[Night Watch](https://www.goodreads.com/book/show/47989.Night_Watch) | City Watch
[Thud!](https://www.goodreads.com/book/show/62530.Thud_) | City Watch
[Snuff](https://www.goodreads.com/book/show/8785374-snuff) | City Watch
[Mort](https://www.goodreads.com/book/show/386372.Mort) | Death
[Reaper Man](https://www.goodreads.com/book/show/34517.Reaper_Man) | Death
[Soul Music](https://www.goodreads.com/book/show/34502.Soul_Music) | Death
[Hogfather](https://www.goodreads.com/book/show/34532.Hogfather) | Death
[Thief of Time](https://www.goodreads.com/book/show/48002.Thief_of_Time) | Death
[The Wee Free Men](https://www.goodreads.com/book/show/34494.The_Wee_Free_Men) | Tiffany Aching
[A Hat Full of Sky](https://www.goodreads.com/book/show/34501.A_Hat_Full_of_Sky) | Tiffany Aching
[Wintersmith](https://www.goodreads.com/book/show/34492.Wintersmith) | Tiffany Aching
[I Shall Wear Midnight](https://www.goodreads.com/book/show/7576115-i-shall-wear-midnight) | Tiffany Aching
[The Shepherd's Crown](https://www.goodreads.com/book/show/22886868-the-shepherd-s-crown) | Tiffany Aching

And that's it. For more information about which book you might like, you can click through to the `goodreads` for synopsis and user reviews.
