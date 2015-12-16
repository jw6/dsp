[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> First the program makes a list of 1000 random values in the range [0.0, 1.0). Then I created a pmf and cdf from the random list and then plotted both. Here are the [pmf graph](fig4.1.png) and the [cdf graph](fig4.2.png).

```
import random
import thinkstats2
import thinkplot

list = [random.random() for _ in range(1000)]

pmf = thinkstats2.Pmf(list, label='list')
cdf = thinkstats2.Cdf(list, label='list')

thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.show(xlabel='value', ylabel='prob')

thinkplot.Cdf(cdf)
thinkplot.show(xlabel='value', ylabel='CDF')
```
