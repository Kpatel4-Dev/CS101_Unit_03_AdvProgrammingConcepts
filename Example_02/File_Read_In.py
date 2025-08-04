# a file named "geek", will be opened with the reading mode.
file = open('example.txt', 'r')
print("Example 1:\n")

# This will print every line one by one in the file
for each in file:
    print (each)

#In this example, we will extract a string that contains all characters in the 
#Python file then we can use file.read(). 
print("\nExample 2:\n")
file = open('example.txt', 'r')
print (file.read())

#Example 3: In this example, we will see how we can read a file using the with statement in Python.

print("\nExample 3:\n")
# Python code to illustrate with()
with open("example.txt") as file:  
    data = file.read() 

print(data)

#Example 4: Another way to read a file is to call a certain number of 
#characters like in the following code the interpreter will read the first five
#characters of stored data and return it as a string: 

print("\nExample 4:\n")
# Python code to illustrate read() mode character wise
file = open("example.txt", "r")
print (file.read(5))

print("\nExample 5:\n")

line = ""
f = open("menu.txt", "r")
line = f.readline()
print(line)
line = f.readline()
print(line)
f.close()

print("\nExample 6:\n")
f = open("menu.txt", "r")
lines = f.readlines()
for food in lines:
  '''
  The rstrip function removes any "whitespace" characters from the end of the   
  string. 
  Whitespace characters include spaces, tabs, and newlines. 
  Make sure you remember to call the rstrip function using parentheses.
  '''
  food = food.rstrip() 
  print("They have %s." % food)
  if food == "roast duck":
    print("Ooo, they have duck!  Yummy!")
    
f.close()

#Another way we could have accomplished OUTPUT of Example: 6 
#-- is to use the singular readline instead of readlines.

print("\nExample 7:\n")
f = open("menu.txt", "r")
food = f.readline()

while food != "":
  food = food.rstrip()
  print("They have %s." % food)
  if food == "roast duck":
    print("Ooo, they have duck!  Yummy!")
  food = f.readline()
  
f.close()

