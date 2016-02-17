# Finding Outliers using ESD

We've all seen bad data points. Those outliers that stick out like a sore thumb and are clearly bad/wrong/irrelevant for whatever reason. These points stick out the most when we try to fit out data. And worse, they seriously change the outcome of our data fits.

Our goal here will be to use the generalized Extreme Studentized Deviant (ESD) Test to automate the process of bad data points, so we can refit our data.

## METHOD

You can find the full iPython document [here](5_esd.ipynb).

1. First, I generated some noisey data in the form of a 2D exponential decay curve and added some bad data points.
2. Then I implemented the ESD Test using `scipy`.
3. Next I fit the data using `scipy.optimize.curve_git` and grabbed the fit parameters.
4. Then I generated a whole new data set, using the parameters I got from `curve_fit`.
5. Then I passed the real data set and the artifically-generated `curve_fit` dataset into my ESD test.
6. Finally, using the bad data points highlight by the ESD test I am able to remove by bad data points and re-fit the data.

## RESULTS

This example is more about the methods than the results. The ESD test is great for any data set that you can easily fit to a function. If your data is a 2D spatial map of a road network or a 3D map of neuron activity in the brain, the ESD test will be less useful.

After playing around with the ESD test some, there are some obvious (though minor) logical limitations. The quality of your fitting function is paramount. And if the portion of bad data points you have is too high, the whole system obviously crumbles. Still, it seems solid for data that are easily fit to a known type of function.

## For Further Reading

#### Least Squares Fitting in Python

In this example we use the Scipy `curve_fit` method. If you would like to try using a least squares fit instead, start with these nice examples.

* [MPIA Python Workshop](https://python4mpia.github.io/fitting_data/least-squares-fitting.html)
* [SciPy Manual](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.lstsq.html)
