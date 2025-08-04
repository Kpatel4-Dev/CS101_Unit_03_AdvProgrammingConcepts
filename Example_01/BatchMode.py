#    Program to create a file of usernames in batch mode.

'''-----------------------------------------------------------------------
fullname(str1)
/* str1 is a string */
Step 1: first we split the string into a list.
Step 2: newspace is initialized by a space("")
Step 3: then traverse the list till the second last word.
Step 4: then adds the capital first character using the upper function.
Step 5: then get the last item of the list.
-----------------------------------------------------------------------'''

# python program to print initials of a name 
def fullname(str1):
   # split the string into a list 
   lst = str1.split()
   newspace = ""
   # traverse in the list 
   for i in range(len(lst)-1):
      str1 = lst[i]
   # adds the capital first character 
      newspace += (str1[0].upper()+'.')
   # l[-1] gives last item of list l.
      newspace += lst[-1].title()
   return newspace 


def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0]+last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)
    
    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

    # Driver code for FullName function  
    print();
    str1=input("Enter Full Name ::>")
    print("Short Form of Name Is ::>",fullname(str1))  

main()
