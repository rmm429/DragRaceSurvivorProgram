#!/usr/bin/python3

import sys
import csv

def countSeasons(s):

    if s == "Season 1":
        seasonsVotes[0] += 1
    elif s == "Season 2":
        seasonsVotes[1] += 1
    elif s == "Season 3":
        seasonsVotes[2] += 1
    elif s == "Season 4":
        seasonsVotes[3] += 1
    elif s == "Season 5":
        seasonsVotes[4] += 1
    elif s == "Season 6":
        seasonsVotes[5] += 1
    elif s == "Season 7":
        seasonsVotes[6] += 1
    elif s == "Season 8":
        seasonsVotes[7] += 1
    elif s == "Season 9":
        seasonsVotes[8] += 1
    elif s == "Season 10":
        seasonsVotes[9] += 1
    elif s == "Season 11":
        seasonsVotes[10] += 1
    elif s == "Season 12":
        seasonsVotes[11] += 1
    elif s == "All Stars 1":
        seasonsVotes[12] += 1
    elif s == "All Stars 2":
        seasonsVotes[13] += 1
    elif s == "All Stars 3":
        seasonsVotes[14] += 1
    elif s == "All Stars 4":
        seasonsVotes[15] += 1
    elif s == "All Stars 5":
        seasonsVotes[16] += 1
    elif s == "Thailand Season 1":
        seasonsVotes[17] += 1
    elif s == "Thailand Season 2":
        seasonsVotes[18] += 1
    elif s == "UK Season 1":
        seasonsVotes[19] += 1
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

        if i <= 12:
            print("Season {}\t\t{}\t{}%".format(i, n, pRound))
        elif 13 <= i <= 17:
            print("All Stars {}\t\t{}\t{}%".format(i - 12, n, pRound))
        elif 18 <= i <= 19:
            print("Thailand Season {}\t{}\t{}%".format(i - 17, n, pRound))
        elif i == 20:
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

            seasonsVotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            print("All Entries:\n")
            totalVotes = parseCSV()
            print("\nTotal Votes\t{}\n".format(totalVotes))

            calcPercent()
    except IndexError:
        print("ERROR: Must supply a CSV file")




