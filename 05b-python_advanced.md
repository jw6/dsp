## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  

Use regular expressions to:

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> \# of different degrees: 8

>> phd: 31

>> scd: 6

>> ms: 2

>> mph: 2

>> md: 1

>> bsed: 1

>> ma: 1

>> jd: 1

>> Also, there is one person in the file without any degrees listed (the zero) but this was ignored with the regular expressions and not inlcuded as a degree.


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> \# of different titles: 3

>>professor: 13

>>assistant professor: 12

>>associate professor: 12

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu', 'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu', 'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu', 'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu', 'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu', 'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu', 'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu', 'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu', 'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']



####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> \# of different domains: 4

>> mail.med.upenn.edu: 23

>> upenn.edu: 12

>> cceb.med.upenn.edu: 1

>> email.chop.edu: 1

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }
```
Print the first 3 key and value pairs of the dictionary:

>> 
```
faculty_dict = {'Bryan': [['PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']], 
'Morales': [['Sc.D.', 'Associate Professor of Biostatistics', 'knashawn@mail.med.upenn.edu']], 
'Bilker': [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']], ...}
```

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

Print the first 3 key and value pairs of the dictionary:

>> 
```
professor_dict1 = {('Scarlett', 'Bellamy'): ['Sc.D.', 'Associate Professor of Biostatistics',
'bellamys@mail.med.upenn.edu'], ('Alisa', 'Stephens'): ['Ph.D.', 'Assistant Professor of Biostatistics',
'alisaste@mail.med.upenn.edu'], ('Warren', 'Bilker'): ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'],  ...}
```

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

>> To be honest, I thought the wording on these questions was very confusing. Since dictionaries are inherently unsorted, I was unsure if I was supposed to just redo the above dictionary in a format of "(Lastname, Firstname): [...]" or actually print the dictionary sorted and even then whether the format was (Firstname, Lastname) or (Lastname, Firstname). So I am supplying all of the ways I interpretted this question.

>> Not printed alphabetically but a dictionary stored "(Lastname, Firstname)":
```
professor_dict2 = {('Localio', 'A.'): ['JD MA MPH MS PhD', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu'], 
('Hsu', 'Yenchih'): ['Ph.D.', 'Assistant Professor of Biostatistics', 'hsu9@mail.med.upenn.edu'], 
('French', 'Benjamin'): ['PhD', 'Associate Professor of Biostatistics', 'bcfrench@mail.med.upenn.edu'], ...}
```

>> professor_dict1 print of last name alphabetical sort:
```
('Scarlett', 'Bellamy') : ['Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker') : ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']
('Matthew', 'Bryan') : ['PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']
```

>> professor_dict2 print of last name alphabetical sort:
```
('Bellamy', 'Scarlett') : ['Sc.D.', 'Associate Professor of Biostatistics', 'bellamys@mail.med.upenn.edu']
('Bilker', 'Warren') : ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']
('Bryan', 'Matthew') : ['PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']
```

>> I am unsure if Q6 and Q7 were also supposed to have been submitted alphabetically but they did not say anything about sorting them. I hope this will be sufficient for my submission.

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

