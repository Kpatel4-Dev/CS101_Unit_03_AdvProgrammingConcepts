#Example 1: In this example, we will see how the write mode and the write() 
#function is used to write in a file. 
#The close() command terminates all the resources in use and frees the system 
#of this particular program. 


# Python code to create a file
print("Example 1:\n")
file = open('example.txt','w')
file.write("This is the write command.")
file.write(" It allows us to write in a particular file.")
file.close()

#Example 2: We can also use the written statement along with the  with() function.

print("\nExample 2:\n")
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f: 
  f.write("Hello World!!!")

#-------------------------------------------------------------------------------------
print("\nExample 3:\n")
infile = open("menu.txt", "r")
print("The current menu on file is:")
for menuitem in infile:
  print(menuitem.rstrip())
infile.close()
print()
 
create_new = input("Would you like to throw away this menu " + "and create a new one? (y/n): ")
 
if create_new == "y":
  outfile = open("NewMenu.txt", "w")
  food = input("What do you want to eat? (Enter nothing to quit.) ")
  while food != "":
    outfile.write(food + "\n")
    food = input("What do you want to eat? (Enter nothing to quit.) ")

  outfile.close()

