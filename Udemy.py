import csv
import os
Title=[]
Price=[]
Subscriber_Count=[]
Reviews=[]
Course_length=[]
length=[]
Subscriber_percent=[]
with open('web_starter.csv','r')as udemyfile:
    udemyrows=csv.reader(udemyfile,delimiter=',')
    for i in udemyrows:
       Title.append(i[1])
       Price.append(i[4])
       Subscriber_Count.append(i[5])
       Reviews.append(i[6])
       Course_length.append(i[9])
       
    for i in Course_length:
       cl=i.split()
       length.append(float(cl[0]))
    for i,j in zip(Reviews,Subscriber_Count):
        Subscriber_percent.append(round(int(i)/int(j),2))
    
    courses=zip(Title,Price,Subscriber_Count,Reviews,length,Subscriber_percent)
# Specify the file to write to
output_path = os.path.join("udemy.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Title','Price','Subcriber Count','Number of Reviews','Course Length','Subscriber_Percentage'])
    csvwriter.writerows(list(courses))
    
