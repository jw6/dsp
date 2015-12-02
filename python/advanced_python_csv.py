import csv
from advanced_python_regex import Faculty

emails = Faculty("faculty.csv").get_emails()
#print(emails)
with open("emails.csv", 'w') as file:
    writer = csv.writer(file, delimiter = "\n")
    writer.writerows([emails])
