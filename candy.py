# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []
candyCart1=[]
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)
for i in range(allowance):
    x=int(input("Enter the candy number :"))
    candyCart.append(candyList[x])
for i in range(len(candyCart)):
    print(candyCart[i])

a=["0","1","2","3","4","5","6","7","8","9"]
y=input("Enter the candy number: ")
while y in a:
    candyCart1.append(candyList[int(y)])
    y=input("Enter the candy number,or type \"I dont want anymore\"")
for i in range(len(candyCart1)):
             print(candyCart1[i])