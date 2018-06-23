import csv
with open ('cereal_bonus.csv','r') as file:
    rowlist=csv.reader(file)
    #csv_header=next(rowlist)
    #print(f"Header:{csv_header}")
    for i in rowlist:
        if float(i[7])>=5:
            print(i)