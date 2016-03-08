# MCSStk1.py

'''Takes stock price date from SQL table and randomizes the date order to
    create a new List
'''


import random
import datetime
import time
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

class getStockData():

    def __init__(self,symbol,IDKey):
        self.symbol = symbol
        self.IDKey = IDKey
        print("Symbol: ",self.symbol,self.IDKey)

        self.conn = sqlite3.connect('allStks.db')
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row
        self.diskEngine = create_engine('sqlite:///allCotEtf.db')

        self.origList = []

        self.newList = []

    def querySQL(self):

        self.fromSQLcursor = self.cursor.execute("SELECT SYMBOL,DATE,CLOSE "
                                   "FROM SymbolsDataDaily "
                                    "WHERE DATE > '2016-02-10'"
                                    " AND SYMBOL = '{0}' ".format(self.symbol))

        self.fromSQLconn = self.conn.execute("SELECT * "
                                   "FROM SymbolsDataDaily "
                                    "WHERE DATE > '2016-02-10' ")

    def originalList(self):
        self.originalListx = []
        for row in self.fromSQLcursor:
            # print(row)
            # print(dict(row))
            # print(row['Symbol'],row['close'])
            self.origList.append(dict(row))

        for row in self.origList:
            self.originalListx.append(dict(row))

        # for row in self.fromSQLconn:
        #     print(row)
        # print('Listx: ',self.originalListx)
        # return self.originalListx

    def drawDay(self):
        pick = random.choice(self.origList)
        return pick

    def randomOrder(self):

        for draw in range(len(self.origList)):
            pick = self.drawDay()
            self.newList.append(pick)
            # print("Pick:",pick['date'])

            counter = 0
            for each in self.origList:
                # print("Each: ",each['date'])
                if each == pick:
                    # print("Bingo",counter)
                    del self.origList[counter]
                    break
                else:
                    counter += 1

        print()
        print("OriginalFullList: {0}".format(self.symbol.upper()))
        print(len(self.originalListx))
        for item in self.originalListx:
            print(item['date'],item['close'])

        print()
        print("RandomOrderList: {0}".format(self.symbol.upper()))
        print(len(self.newList))
        for item in self.newList:
            print(item['date'],item['close'])

    def tempTest(self):
        x = [5,10,15,20]
        y = x
        print()
        print("del from list test")
        print(y)
        del x[2]
        print(x,y)

def main():
    symbol = input("Enter Symbol to be randomized: ")
    # symbol = 'AAPL'
    IDKey = 99
    a = getStockData(symbol,99)
    a.querySQL()
    a.originalList()
    a.randomOrder()

    a.tempTest()

if __name__ == '__main__':main()