#!/usr/bin/python3

import sys
import csv

def countSeasons(s):

    if s == "Season 3":
        seasonsVotes[0] += 1
    elif s == "Season 5":
        seasonsVotes[1] += 1
    elif s == "Season 6":
        seasonsVotes[2] += 1
    elif s == "Season 9":
        seasonsVotes[3] += 1
    elif s == "Season 12":
        seasonsVotes[4] += 1
    elif s == "All Stars 2":
        seasonsVotes[5] += 1
    elif s == "Thailand Season 2":
        seasonsVotes[6] += 1
    elif s == "UK Season 1":
        seasonsVotes[7] += 1
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

        if i == 1:
            print("Season 3\t\t{}\t{}%".format(n, pRound))
        elif 2 <= i <= 3:
            print("Season {}\t\t{}\t{}%".format(i + 3, n, pRound))
        elif i == 4:
            print("Season 9\t\t{}\t{}%".format(n, pRound))
        elif i == 5:
            print("Season 12\t\t{}\t{}%".format(n, pRound))
        elif i == 6:
            print("All Stars 2\t\t{}\t{}%".format(n, pRound))
        elif i == 7:
            print("Thailand Season 2\t{}\t{}%".format(n, pRound))
        elif i == 8:
            print("UK Season 1\t\t{}\t{}%".format(n, pRound))
        else:
            print("ERROR: Case out of bounds ({})\n".format(i))

        i += 1


if __name__ == "__main__":
    try:
        csvFile = sys.argv[1];
        with open(csvFile, newline='') as csvfile:
            seasons = csv.reader(csvfile, delimiter=',')
            next(seasons)

            seasonsVotes = [0, 0, 0, 0, 0, 0, 0, 0]

            print("All Entries:\n")
            totalVotes = parseCSV()
            print("\nTotal Votes\t{}\n".format(totalVotes))

            calcPercent()
    except IndexError:
        print("ERROR: Must supply a CSV file")




