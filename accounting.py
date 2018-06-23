import csv
with open ('/Users/dhanu/Desktop/MyProjects/MyProjects/accounting.csv','r')as file:
     reader=csv.reader(file)
     for row in reader:
         print(row[0])