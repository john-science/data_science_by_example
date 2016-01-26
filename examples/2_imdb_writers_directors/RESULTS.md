# Parsing IMDB for Writers & Directors

I, like most people, know the names of my favorite actors/actresses. But it occurred to me that I didn't really know who my favorite directors or movie writers are. I knew a few choice names, but that is all.

The idea is that I could use the vast Internet Movie Database ([IMDB](https://www.imdb.com/)) to cross reference all my movies, based on my person ratings, with the writers and directories.

## Methods

#### Data Cleanup

1. IMDB has a huge amount of data available for free [here](http://www.imdb.com/interfaces). I download the writers, directors, and user ratings.
2. In an [iPython](http://ipython.org/) notebook I trimmed all the data using [pandas](http://pandas.pydata.org/), to remove anything that wasn't a movie (TV shows, music videos, video games, etc). I also re-formatted to a simple CSV.

The data cleanup notebook is [here](trim_imdb_data.ipynb).

#### Analysis

1. In `iPython`, I read all three datasets (writers, directors, and ratings) into `pandas` dataframes, and used built-in Pandas fucntions to remove duplicates and null values.
2. I then defined a couple functions to rank writers and directors based on the IMDB ratings of their movies, with a cut for movies that only had a few votes on IMDB.
3. Then, because I have been an IMDB member since the very early days, I was able to download an ingest my personal ratings over about 700 movies.
4. Finally, I was able to use built-in `pandas` functions to combine the writers and directors with my personal ratings of movies to determine which writers and directors are my favorites.

The data analysis notebook is [here](imdb_writers_directors.ipynb).

## Results

In the end, I actually generated two completely separate sets of results. I determine which writers and directors were my favorites, which was my goal. But I also the more generally intersting set of writers and directors voted best by IMDB users.

#### My Favorites

Apparently, my favorite directors are:

Directors | Writers
:-- | :--
Gilliam, Terry | Gilliam, Terry
Hitchcock, Alfred | Chapman, Graham
Coen, Joel | Coen, Joel
Coen, Ethan | Coen, Ethan
Jackson, Peter | Jackson, Peter
Spielberg, Steven | Walsh, Fran
Anderson, Wes | Anderson, Wes
Scott, Ridley | Idle, Eric
Kubrick, Stanley | Kubrick, Stanley 
Jones, Terry | Jones, Terry

Some of this I already knew. My abiding love for Monty Python and classic Terry Gilliam was not a suprise. I was suprised to realize that Peter Jackson and Steven Spielberg made the list, but there they are.

#### IMDB People's Choice Awards

More interesting is probably the 25 top writers and directors of IMDB, based on user movie ratings:

Directors | Writers
:-- | :--
Hitchcock, Alfred | Kurosawa, Akira
Kurosawa, Akira | Hecht, Ben
Scorsese, Martin | Wilder, Billy
Bergman, Ingmar | Bergman, Ingmar
Spielberg, Steven | Allen, Woody
Allen, Woody | Miyazaki, Hayao
Wilder, Billy | Shakespeare, William
Wyler, William | Huston, John
Hawks, Howard | Oguni, Hideo
Eastwood, Clint | Buñuel, Luis

Notable, some people are on both the favorite writers and favorite directors list:

* Kurosawa, Akira
* Wilder, Billy
* Bergman, Ingmar
* Allen, Woody

Digging into this more, it becomes clear there is even more overlap between the top 100 writers and directors. Perhaps this is because a great director has to understand good storytelling. Or perhaps a movie that has a single artistic goal from start to finish can be better. Whatever the reason, the overlap between the two initially separate datasets is clearly important.

I learned two more interesting things:

1. I should watch more Kurosawa movies.
2. Even though he died 300 years before movies became popular, Shakespeare is still a dominate writer in our culture.
