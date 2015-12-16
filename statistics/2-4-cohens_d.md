[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The Cohen's *d* value that I obtained was ~ -0.089 standard deviations between the mean total weight of first born babies and others (first born babies weighing less). This is a larger difference than that of mean pregnancy length, but still an insignificant difference. The code I used is below:

```
import nsfg
import math


def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

print("The Cohen's d of total weight for first babies and others is: {}".format(d))
```

```
Output: The Cohen's d of total weight for first babies and others is: -0.08867292707260174
```
