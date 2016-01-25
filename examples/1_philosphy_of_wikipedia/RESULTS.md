# 1. Philosophy of Wikipedia

Randal Monroe, of XKCD, [posited the theory](https://xkcd.com/903/) that if you start on any Wikipedia page and click the first link, then click the first link on the next page, and so on, you will eventually end up on the Philosophy page.

I can not firmly attribute this idea to him, XKCD is just the first place I ran into it. But I thought it would be a fun theory to test.

## Method

This is the first example in this repository because it was so easy to solve: it only took two simple Python functions. Working in an [iPython](http://ipython.org/) notebook, there were three basic steps:

1. Write a function using [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/) and [requests](http://docs.python-requests.org/en/latest/) to scrap a Wikipedia article to find the first link.
2. Write a function the follows the links returned from the first function until you hit the Philosophy page, or entered an infinite loop.
3. Play around with the second function, trying many, many options and looking for patterns.

Full solution [here](philosophy_of_wikipedia.ipynb).

## Results

Broadly speaking, the theory holds up. I say "broadly" because there are a couple of notable exceptions. There appear to be a few infinite loops among the Wikipedia links. And based on various internet articles, I believe some Wikipedia editors created infinite loops specifically to disprove the XKCD theory.

But following the first links *nearly* always gets you to Philosophy. Still, playing around a bit, you'll find a couple of other intersting patterns.

#### HOW does the page get to philosophy?

It turns out that a great many pages eventually funnel down to the taking the same path to the Philosophy page:

* Science
* Knowledge
* Awareness
* Conscious
* Quality_(philosophy)
* Philosophy

So we could also say that following the first link of each Wikipedia article will eventually lead you to the Science page. Though, it turns out, this is slightly less true.

#### Then what?

Okay, after a page reach Philosophy, what happens if you keep following the first links?

* Philosophy
* Reality
* Existence
* Ontology
* Philosophy

It's an infinite loop! This is a MUCH stronger statement about the nature of these first links in Wikipedia articles:

> Following the first link of Wikipedia articles will nearly always lead to the Philosophy article, and then be stuck in an infinite loop with the Philosophy article at the head.
