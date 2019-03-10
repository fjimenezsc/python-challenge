import os
import csv

print("Financial Analysis")
print("--------------------------")

file = open("budget_data.csv")
numline = len(file.readlines())
print(f"Total months: {numline - 1}")

pl = []

with open("budget_data.csv", "r") as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)
    for row in csvread:
        pl.append(int(row[1]))

    print(f"Total ${sum(pl)}")

average_change = (sum(pl)/(numline - 1))
print(average_change)

write_file = "Pybank_results.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total months: {numline - 1}\n")
filewriter.write(f"Total ${sum(pl)}\n")

filewriter.close()  