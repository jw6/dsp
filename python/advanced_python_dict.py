import re

class Faculty(object):

    def __init__(self, data):
        self.data = data
        with open(data) as file:
            parsed_data = file.read()
        self.parsed_data = parsed_data
        #print(parsed_data)

    def get_all(self):
        all = re.findall(r'''
            ^(?P<name>(?P<firstname>[\w.]+)\s?(?P<middlename>\(?[\w.]*\)?)\s(?P<lastname>[\w.]+)),\s?
            (?P<degrees>[\w.\s]+),\s?
            (?P<title>[\s\w]+),\s?
            (?P<email>[-\w.+]+@[-\w\d.]+)$
        ''', self.parsed_data, re.X|re.M)
        #print(all)

        faculty_dict = {}
        for person in all:
            if person[3] not in faculty_dict:
                faculty_dict[person[3]] = []
            faculty_dict[person[3]].append(list(person[4:]))
        print("faculty_dict = {}\n\n".format(faculty_dict))
        #print("\n\n{}".format(faculty_dict['Li']))

        professor_dict1 = {}
        for person in all:
            professor_dict1[(person[1], person[3])] = list(person[4:])
        print("professor_dict1 = {}\n\n".format(professor_dict1))

        professor_dict2 = {}
        for person in all:
            professor_dict2[(person[3], person[1])] = list(person[4:])
        print("professor_dict2 = {}\n\n".format(professor_dict2))

fac = Faculty("faculty.csv")
fac.get_all()
