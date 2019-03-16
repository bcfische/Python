import csv
with open("election_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    totalvotes = 0
    candidates = {}
    for row in csvreader:
        totalvotes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
outstring = "-----------------------\n"
outstring += f"Total Votes: {totalvotes}\n"
outstring += "-----------------------\n"
for k,v in candidates.items():
    outstring += f"{k}: {round(100*v/totalvotes,1)}% ({v})\n"
outstring += "-----------------------\n"
maxkey, maxval = max(candidates.items(), key=lambda k: k[1])
outstring += f"Winner: {maxkey}\n"
outstring += "-----------------------"
print(outstring)
f = open("results.txt", "w")
f.write(outstring+"\n")
f.close()