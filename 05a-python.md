# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists do exactly what they sound like, they are used to store a list of values. An example would be:

>> x = ["Ken", "Myers", 1992]
  
>> Tuples are similar to lists in that they can also be used to store values, however they are immutable. An example of a tuple is:
  
>> y = ("Ken", "Myers", 1992)
  
>> Tuples can not be changed once they are created, unlike strings. Due to their immutability, tuples are assigned hash values which allow them to be used as keys in dictionaries. Dictionaries are a list of key-value pairs, the key can be searched in the dictionary to get its corresponding value. The dictionary keys must be immutable because if they were changed, the hash would also change and so the previously associated hash will no longer be able to find the value that the key originally pointed to. This is why tuples can be used as keys but lists can not.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar because they can both be used to store a range of values. They differ in that a set is unordered while a list is ordered. Sets also do not permit duplicates, while lists do. Sets are like dictionaries without the values associated with the keys. The items in a set are hashable. When trying to find an element in either a list or a set, it will be faster to find it in a set than a list because the items in a set are mapped by the hash. What this means is that when search for an item in a set, it needs only check the hash if it is present, while in a list, it must compare every single item to check equivalency.

>> Example of a list: kenncann = ["kenn", "cann"]

>> Example of a set: set(kenncann)

>> Another set example: kenncann = {"kenn", "cann"}


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





