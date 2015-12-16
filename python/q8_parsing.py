#The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

class Football(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
        file = open(self.data)
        with file:
            parsed_data = [row for row in csv.reader(file.read().splitlines())]
        #print(parsed_data)
        return parsed_data

    def get_min_score_difference(self, parsed_data):
        del parsed_data[0]
        goals = [line[5] for line in parsed_data]
        goals_allowed = [line[6]for line in parsed_data]
        differences = [float(x) - float(y) for x, y in zip(goals, goals_allowed)]
        return differences.index(min(differences))


    def get_team(self, index_value, parsed_data):
        minTeam = parsed_data[index_value][0]
        print("The team with the minimum difference in goals scored and allowed was {}.".format(minTeam))

#Test of the above class
testFootball = Football("football.csv")
data = testFootball.read_data()
minDiff = testFootball.get_min_score_difference(data)
testFootball.get_team(minDiff, data)
