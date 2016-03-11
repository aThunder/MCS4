# MCSBday.py

'''Assuming an even distribution of birthdays in a non-leap year, how many people need to be in a room for there to be a greater than
   50% chance of two of them having the same birthday? How many people for there to be a greater than a 99% chance of
   two people having the same birthday?

1. Create a list of numbers 1-365
2. Randomly select 2 numbers from the list (after a number is picked it stays in the available list)
3. Check to see if 2 of the randomly picked numbers match
   As soon as the first match is found stop checking for matches (this is the adjustment I mentioned above)
4. Run this test x number of times, count the number of total matches and divide by x
5. Increase the number of randomly selected numbers by 1 and repeat steps 2-5 (now using the new +1 number in step 2)
   Once step 4 results in a number > 99% stop the program.

'''


import numpy as np
import random

class MatchBirthdays():

    def __init__(self):
        self.allBdaysList = []
        self.matches = []

    def buildList(self):
        # self.matches = 0

        for i in range(1,366):
            self.allBdaysList.append(i)


    def testSpecificNumberOfPeople(self,tests,people):
        self.people = people
        self.tests = tests
        allPicks = []
        # seen = []
        # counter = 0
        self.matches = 0

        for test in range(tests):
            self.allPicks = []
            # matches = 0
            self.seen = []
            for inRoom in range(people):
                    # print("inRoom: ", inRoom)
                    pick = random.choice(self.allBdaysList)
                    self.allPicks.append(pick)


            for value in self.allPicks:
                # print("Value: ", value)
                if value not in self.seen:
                    self.seen.append(value)
                else:
                    self.matches +=1
                    # print("Match")
                    # print("Value: ",value)
                    # print("Matched: ",allPicks)
                    # print("Match")
                    # print("allPicks: ",allPicks)
                    break

    def printResult(self):
        print("People: {0}, Matches: {1}, PercentMatch: {2}".format(self.people,self.matches,(self.matches/self.tests)*100))

def main():
    a = MatchBirthdays()
    a.buildList()
    for i in range(57,60):
        a.testSpecificNumberOfPeople(2000000,i)
        a.printResult()



if __name__ == '__main__':main()