# Parsing IMDB for Writers & Directors

I, like most people, know the names of my favorite actors/actresses. But it occurred to me that I didn't really know who my favorite directors or movie writers are. I knew a few choice names, but that is all.

The idea is that I could use the vast Internet Movie Database ([IMDB](https://www.imdb.com/)) to cross reference all my movies, based on my person ratings, with the writers and directories.

## Methods

IMDB makes huge amounts of their data available for free [here](http://www.imdb.com/interfaces).

I downloaded the data files for writers, directors, and user ratings, and in an [iPython](http://ipython.org/) notebook trimmed all of their data using [pandas](http://pandas.pydata.org/), to create new CSV files. This is a common step in data analysis. The IMDB data file were in a custom, hard-to-read format. So I converted them to CSV. I also removed a lot of data I didn't want. I only wanted to look at movies, but the IMDB data files includes extensive information on television, music videos, video games, and more.

The data cleanup notebook is [here](2_imdb_writers_directors/trim_imdb_data.ipynb).

TODO

## Results

TODO
