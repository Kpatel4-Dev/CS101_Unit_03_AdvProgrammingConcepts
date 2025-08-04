#! /usr/bin/python

# Programmer: Kavita Patel 
# Date:  11/9/2024      
#
# Get the strings in input.txt and put them into a list
# Add the 2 numbers in each string of that list and put them in output.txt.


def main():
    print("Add the 2 numbers in each line of input.txt and send the sum values to output.txt")
    # First get -- create a list from the input file
    # Open file
    infile = open("input.txt", "r")
    lines = []
    for line in infile:
        lines.append(line)
    # Close file
    infile.close()
    
    # Print a message to the screen
    print("Print the values to the screen and to the file output.txt")

    outfile = open("output.txt", "w")
    for line in lines:
        array_of_numbers = line.split()
        print(array_of_numbers)
        sum = int(array_of_numbers[0]) + int(array_of_numbers[1])
        print(sum)
        print(sum, file=outfile)

    outfile.close
main()


''' 
Click the add file button, create a .txt file to input data, which will be 
read by the file read().
'''
#This opens the file programmatically, reads the data in the file into a variable
#called contents, closes the file, and prints the file contents to our output 
#pane.

'''
f = open("input.txt")
contents = f.read()
f.close()
print(contents)
'''
'''
Instead of manually creating files, you can also use Python to do this. Add the following code to your main.py file.
'''
'''
f = open("createdfile.txt", "w")
f.write("This is some data that our Python script created.\n")
f.close()
'''
'''
Note the w argument that we pass into the open function now. This means that we want to open the file in "write" mode. Be careful: if the file already exists, Python will delete it and create a new one. There are many different 'modes' to work with files in different ways which you can read about in the Python documentation.
'''
