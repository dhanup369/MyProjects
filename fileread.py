file = '/Users/dhanu/Desktop/input.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:
   for line in text:
       print (line)
    #print(text)

    # Store all of the text inside a variable called "lines"
    #lines = text.readlines()
    #lines = [text.strip('\n') for line in lines]

    # Print the contents of the text file
    #print(lines==lines)
