import re
import collections

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

        sorted_professor_dict1 = collections.OrderedDict(sorted(professor_dict1.items(), key=lambda x: x[0][1]))
        print("\n\nFirst professor_dict sorted by lastname\n")
        for k, v in sorted_professor_dict1.items(): print("{} : {}".format(k,v))

        sorted_professor_dict2 = collections.OrderedDict(sorted(professor_dict2.items()))
        print("\n\nSecond professor_dict sorted by lastname\n")
        for k, v in sorted_professor_dict2.items(): print("{} : {}".format(k,v))

fac = Faculty("faculty.csv")
fac.get_all()
