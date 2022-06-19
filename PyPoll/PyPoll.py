
import os
import csv


cwd = os.getcwd()

csvpath = os.path.join(cwd,"Resources","election_data.csv")

votes = set()
names = set()
cand = []

with open(csvpath,encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    next(csvreader, None)

    for row in csvreader:
        votes.add(int(row[0]))
        names.add(str(row[2]))
        cand.append(str(row[2]))

    names = list(names)
    votes = list(votes)
    
    vote1 = cand.count(names[0])
    vote2 = cand.count(names[1])
    vote3 = cand.count(names[2])
    
    perc1 = (vote1 / len(votes)) *100
    perc2 = (vote2 / len(votes)) *100
    perc3 = (vote3 / len(votes)) *100

    
    if vote1 > vote2 and vote1 > vote3:
        winner=(names[0])
    elif vote2 >vote1 and vote2 > vote3:
        winner=(names[1])
    else:
        winner=(names[2])

    print(f"Election Results\n--------------------")
    print(f"Total Votes: {len(votes)}\n--------------------")
    print(f"{names[0]}: {round(perc1,3)}% ({vote1})")
    print(f"{names[1]}: {round(perc2,3)}% ({vote2})")
    print(f"{names[2]}: {round(perc3,3)}% ({vote3})\n--------------------")
    print(f"{winner}\n--------------------")
    
    textpath = os.path.join(cwd,"analysis","Election Results.txt")

    with open(textpath,"w") as f:
        print("created text file")
        f.write(f"Election Results\n--------------------\n")
        f.write(f"Total Votes: {len(votes)}\n--------------------\n")
        f.write(f"{names[0]}: {round(perc1,3)}% ({vote1})\n")
        f.write(f"{names[1]}: {round(perc2,3)}% ({vote2})\n")
        f.write(f"{names[2]}: {round(perc3,3)}% ({vote3})\n--------------------\n")
        f.write(f"{winner}\n--------------------")
    



 



    

