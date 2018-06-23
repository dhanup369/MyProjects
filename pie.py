print("Welcome to the House of Pies! Here are our pies: "+"\n"+
      "------------------------------------------------------"+"\n"+
      "(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak")

r="Yes"
o=[]
pie=["Pecan","Apple Crisp","Bean","Banoffee", "Black Bun", "Blueberry","Buko","Burek","Tamale","Steak"]
while r=="Yes":
    x=int(input("Order the number next to the pie you want: "))
    y=pie[x-1]
    o.append(y)
    print("Great! We'll have that "+y+" right out for you")
    z=input("Would you like to make another order?Type Yes or No:  ")
    r=z
print ("Total number of pies ordered: ",len(o))
for i in range(len(o)):
    print (o.count(o[i]),o[i])
