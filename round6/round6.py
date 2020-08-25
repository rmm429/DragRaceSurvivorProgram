#!/usr/bin/python3

import sys
import csv

def countSeasons(s):

    if s == "Season 2":
        seasonsVotes[0] += 1
    elif s == "Season 3":
        seasonsVotes[1] += 1
    elif s == "Season 4":
        seasonsVotes[2] += 1
    elif s == "Season 5":
        seasonsVotes[3] += 1
    elif s == "Season 6":
        seasonsVotes[4] += 1
    elif s == "Season 8":
        seasonsVotes[5] += 1
    elif s == "Season 9":
        seasonsVotes[6] += 1
    elif s == "Season 10":
        seasonsVotes[7] += 1
    elif s == "Season 12":
        seasonsVotes[8] += 1
    elif s == "All Stars 2":
        seasonsVotes[9] += 1
    elif s == "All Stars 3":
        seasonsVotes[10] += 1
    elif s == "All Stars 4":
        seasonsVotes[11] += 1
    elif s == "Thailand Season 1":
        seasonsVotes[12] += 1
    elif s == "Thailand Season 2":
        seasonsVotes[13] += 1
    elif s == "UK Season 1":
        seasonsVotes[14] += 1
    else:
        print("ERROR: Invalid entry ({})\n".format(s))


def parseCSV():
    totalVotes = 0

    for row in seasons:
        totalVotes += 1
        print("\t{}".format(row[1]))
        countSeasons(row[1])

    return totalVotes

def writeCSV(s, n, p):
    with open(csvWrite, mode='a') as results_file:
        results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results_writer.writerow([s, n, p])

def calcPercent():
    i = 1
    for n in seasonsVotes:
        p = (n / totalVotes) * 100
        pRound = "{}%".format(round(p, 3))
        season = ""

        if i <= 5:
            season = "S{}".format(i + 1)
        elif 6 <= i <= 8:
            season = "S{}".format(i + 2)
        elif i == 9:
            season = "S{}".format(i + 3)
        elif 10 <= i <= 12:
            season = "AS{}".format(i - 8)
        elif 13 <= i <= 14:
            season = "DRT{}".format(i - 12)
        elif i == 15:
            season = "DRUK{}".format(i - 14)
        else:
            print("ERROR: Case out of bounds ({})\n".format(i))

        print("{}\t\t{}\t\t{}".format(season, n, pRound))

        if len(sys.argv) > 2:
            writeCSV(season, n, pRound)

        i += 1


if __name__ == "__main__":
    try:
        csvRead = sys.argv[1]
        csvWrite = ""
        if len(sys.argv) > 2:
            csvWrite = sys.argv[2]

        with open(csvRead, newline='') as csvfile:
            seasons = csv.reader(csvfile, delimiter=',')
            next(seasons)

            seasonsVotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            print("All Entries:\n")
            totalVotes = parseCSV()
            print("\nTotal Votes\t{}\n".format(totalVotes))

            if len(sys.argv) > 2:
                writeCSV('Season', 'Votes', 'Percentage')

            calcPercent()
    except IndexError:
        print("ERROR: Must supply a CSV file")




