import csv
with open ('netflix_ratings.csv','r') as file:
    rowlist=csv.reader(file)
    rows=[]
    for i in rowlist:
        rows.append(i)
    #print(rows[0])
    title=[]
    for i in rows:
         title.append(i[0])
    #title=list that contains all the movie names
    usermovie=input("Enter the movie name: ")
    userlist=[]
    if usermovie in title:
        movie_index=title.index(usermovie)
        userlist=rows[movie_index]
        print(usermovie,"is rated ",userlist[1],"with the rating of ",userlist[5])
    else:
        print("User Video could not be found")