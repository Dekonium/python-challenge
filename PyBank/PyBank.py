import os
import csv

cwd = os.getcwd()

csvpath = os.path.join(cwd,"Resources","budget_data.csv")

months = 0
total = 0
change = 0

val = []
date = []

with open(csvpath,encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next(csvreader, None)

    for row in csvreader:
        
        months += 1
        
        money = int(row[1])
        
        total = total + money
        
        val.append(int(row[1]))
        date.append(str(row[0]))
        
    change = total / months
   
    maxval = (max(val))
    minval = (min(val))

    maxind=(val.index(maxval))
    minind=(val.index(minval))


    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${change}")
    print(f"Greatest Increase in Profits : {date[maxind]} (${maxval})")
    print(f"Greatest Decrease in Profits : {date[minind]} (${minval})")

textpath = os.path.join(cwd,"analysis","Financial Analysis.txt")

with open(textpath,"w") as f:
    print("created text file")
    f.write(f"Financial Analysis\n---------------------------")
    f.write(f"\nTotal Months: {months}")
    f.write(f"\nTotal: ${total}")
    f.write(f"\nAverage Change: ${change}")
    f.write(f"\nGreatest Increase in Profits : {date[maxind]} (${maxval})")
    f.write(f"\nGreatest Decrease in Profits : {date[minind]} (${minval})")

