import os
import csv

print("Election Results")
print("--------------------------")

file = open("election_data.csv")
numline = len(file.readlines())
print(f"Total votes: {numline - 1}")


print("--------------------------")

candidates = []


with open("election_data.csv", "r") as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)
    for row in csvread:
        candidates.append(str(row[2]))
    unique_candidates = set(candidates)

    print(unique_candidates)

write_file = "Pypoll_results.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total votes: {numline - 1}\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Kahn: \n")
filewriter.write(f"Correy: \n")
filewriter.write(f"Li: \n")
filewriter.write(f"O´Tooley: \n")
filewriter.write("--------------------------\n")
filewriter.write(f"Winner: \n")
filewriter.write("--------------------------\n")

filewriter.close()  

# candidate0 = []
# candidate1 = []
# candidate2 = []
# candidate3 = []


#     for row in csvread:

#     if == unique_candidates(0)
#         candidate0.append(int(row[2]))

#     print(candidate0)
        

