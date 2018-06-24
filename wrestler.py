import csv
import math
with open ('wrestler.csv','r') as file:
    rowlist=csv.reader(file)
    csv_header=next(rowlist)
    print(f"Header:{csv_header}")
    user=input("Enter the wrestler name: ")
    for i in rowlist:
        totalmatches=int(i[1])+int(i[2])+int(i[3])
        if i[0]==user:
            Pass=round((int(i[1])/totalmatches)*100,2)
            Fail=round((int(i[2])/totalmatches)*100,2)
            Draw=round((int(i[3])/totalmatches)*100,2)
            print("Pass Percentage: ",Pass)
            print("Fail Percentage: ",Fail)
            print("Draw Percentage: ",Draw)
            if Fail<50:
                 print("Bummer")       
            else:
                 print("Great Player")