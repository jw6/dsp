import csv
import re
from collections import Counter

class Faculty(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
        file = open(self.data)
        with file:
            parsed_data = [row for row in csv.reader(file.read().splitlines())]
        #print(parsed_data)
        return parsed_data

    def count_degrees(self):
        parsed_data = self.read_data()
        degree_list = []
        del parsed_data[0]

        for row in parsed_data:
            row[1] = row[1].replace(".", "")
            #print(row[1])
            line = re.findall(r'[A-Za-z]+', row[1].lower(), re.X)
            for item in line:
                degree_list.append(item)

        #print(degree_list)
        degree_dict = Counter(degree_list)
        print('# of different degrees: {}'.format(len(degree_dict)))
        #print(degree_dict)
        for k, v in degree_dict.most_common():
            print(k+': '+str(v))

    def count_titles(self):
        parsed_data = self.read_data()
        title_list = []
        del parsed_data[0]

        for row in parsed_data:
            #print(row[2])
            line = re.findall(r'[asociaten]*\s?professor', row[2].lower(), re.X)
            for item in line:
                title_list.append(item)

        #print(title_list)
        title_dict = Counter(title_list)
        print('# of different titles: {}'.format(len(title_dict)))
        #print(title_dict)
        for k, v in title_dict.most_common():
            print(k+': '+str(v))

    def get_emails(self):
        parsed_data = self.read_data()
        email_list = []
        del parsed_data[0]

        for row in parsed_data:
            #print(row[2])
            line = re.findall(r'[-\w.+]+@[.\w]+', row[3].lower(), re.X)
            for item in line:
                email_list.append(item)

        return email_list

    def email_domains(self):
        emails = self.get_emails()
        domain_list = []

        for email in emails:
            domains = re.findall(r'@[\w.]+', email)
            domains[0] = domains[0][1:]
            for domain in domains:
                domain_list.append(domain)

        domain_dict = Counter(domain_list)
        print('# of different domains: {}'.format(len(domain_dict)))
        #print(domain_dict)
        for k, v in domain_dict.most_common():
            print(k+': '+str(v))


#testFaculty = Faculty("faculty.csv")
#data = testFaculty.read_data()
#testFaculty.count_degrees()
#testFaculty.count_titles()
#print(testFaculty.get_emails())
#testFaculty.email_domains()
