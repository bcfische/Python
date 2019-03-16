import csv
with open("budget_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months = 0
    total = 0
    delta_sum = 0
    delta_max = 0
    delta_min = 0
    for row in csvreader:
        months += 1
        total += int(row[1])
        if months>1:
            delta = int(row[1])-pl
            if delta>delta_max:
                delta_max = delta
                date_max = row[0]
            if delta<delta_min:
                delta_min = delta
                date_min = row[0]
            delta_sum += delta
        pl = int(row[1])
outstring = f"Total Months: {months}\n"
outstring += f"Total: ${total}\n"
outstring += f"Average Change: ${round(delta_sum/(months-1),2)}\n"
outstring += "Greatest Increase in Profits: "+date_max+" ($"+str(delta_max)+")\n"
outstring += "Greatest Decrease in Profits: "+date_min+" ($"+str(delta_min)+")"
print(outstring)
f = open("results.txt", "w")
f.write(outstring+"\n")
f.close()