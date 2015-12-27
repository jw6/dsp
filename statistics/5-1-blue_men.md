[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> I began with the example file provided by the book. I added a function to convert from inches to cm and then used these values with scipy.stats.norm's "cdf" method. I subtracted the lower cdf from the upper cdf to get the probability in between the two heights. Approximately 34.27% of men are eligible for the Blue Men Group.

```
import thinkstats2
import thinkplot
import scipy.stats

def in_to_cm(inches):
    return inches*2.54

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

lheight = in_to_cm(70)
uheight = in_to_cm(73)

bluemenprob = dist.cdf(uheight) - dist.cdf(lheight)

print("{}% of men have eligible height for the Blue Men Group".format(round(bluemenprob*100,2)))
```

Output:

```
34.27% of men have eligible height for the Blue Men Group
```
