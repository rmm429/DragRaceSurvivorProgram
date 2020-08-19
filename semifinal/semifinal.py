#!/usr/bin/python3

import sys
import csv

def countSeasons(s):

    if s == "Season 5":
        seasonsVotes[0] += 1
    elif s == "Season 6":
        seasonsVotes[1] += 1
    elif s == "All Stars 2":
        seasonsVotes[2] += 1
    else:
        print("ERROR: Invalid entry ({})\n".format(s))


def parseCSV():
    totalVotes = 0

    for row in seasons:
        totalVotes += 1
        print("\t{}".format(row[1]))
        countSeasons(row[1])

    return totalVotes

def calcPercent():
    i = 1
    for n in seasonsVotes:
        p = (n / totalVotes) * 100
        pRound = round(p, 3)

        if 1 <= i <= 2:
            print("Season {}\t\t{}\t{}%".format(i + 4, n, pRound))
        elif i == 3:
            print("All Stars 2\t\t{}\t{}%".format(n, pRound))
        else:
            print("ERROR: Case out of bounds ({})\n".format(i))

        i += 1


if __name__ == "__main__":
    try:
        csvFile = sys.argv[1];
        with open(csvFile, newline='') as csvfile:
            seasons = csv.reader(csvfile, delimiter=',')
            next(seasons)

            seasonsVotes = [0, 0, 0]

            print("All Entries:\n")
            totalVotes = parseCSV()
            print("\nTotal Votes\t{}\n".format(totalVotes))

            calcPercent()
    except IndexError:
        print("ERROR: Must supply a CSV file")




