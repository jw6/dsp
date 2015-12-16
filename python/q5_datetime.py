from datetime import datetime

formatsList = ["%m-%d-%Y",
"%m%d%Y",
"%d-%b-%Y"]

datesList = [
['01-02-2013', '07-28-2015'],
['12312013', '05282015'],
['15-Jan-1994', '14-Jul-2015']
]

def dayCount (firstDay, lastDay, i):
    a = datetime.strptime(firstDay, formatsList[i])
    b = datetime.strptime(lastDay, formatsList[i])
    delta = b-a
    print(delta.days)

i=0
for x,y in datesList:
    dayCount(x,y,i)
    i+=1
