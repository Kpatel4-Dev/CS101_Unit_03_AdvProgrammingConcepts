# Lab 06 - File Input and Output

## Introduction

Being able to manipulate files with reading and writing is one of the most important tools a programmer can have. Thankfully Python is one of the easiest languages to get started with file input and output!

For file input/output you do not need to import anything in Python. You are able to access a file in one line of code!

To open the file you use the **open(file, access)** function. The function requires 2 parameters no matter what, first parameter is the file name as a string(If you wanted to use a file not in the same directory then you would use the file full file path and the name of the file as the string), and the second parameter is how you would like to access the file. Lastly, if you are going to open a file you need to assign it to a variable, that way you can perform the reading and writing functions on the variable. 

Whenever you **open()** a file you must always **close()** it! If a file is not closed then your changes will not be saved, also in some cases you are hogging up resources on the system.

*There are 3 basic ways to access a file*:

**Reading** 'r' - Access a file that exists, prepare to read its contents. 

**Writing** 'w' - Access a file that may or may not exist, if it doesn't exist create it. Prepare to write at the start of the file, erasing the previous content.

**Appending** 'a' - Access a file that may or may not exist, if it doesn't exist create it. Prepare to write at the end of the file, keeping the previous content.

To designate which one you want to use you must write either 'r', 'w', or 'a' in the 2nd parameter of open().

## Instructions 

### Step 1

With your group you are going to create a file named Favorite Foods and open it for writing because it does not exist yet. Assign it to the variable *food_file*. **Remember you must always close a file when you are finished using it**...so you should create your close statement as soon as you make the open statement.

   food_file = open("Favorite Foods", 'w')
   #Your code goes here
   food_file.close()

If you hit run you will notice that the file is now created in the **Files** section and when you open the file it is empty. 

Now each one of your group members is going to add a line to the file with your first name and favorite food. To do this you simply use the food_file variable and the write() function. In the parameters of the write function is what we want to write, I will give you an example of what I would write: 

   food_file.write("Kyle Cookies\n")

You may have noticed the \n at the end, that is because I want the next name and food to be on the next line. 
One thing you may not have realized is that *whitespace, new-line, and tab* are characters! When you are dealing with files you need to be very specific with every **line** and **space** you read or write.
---
### Step 2 

After all of you have put your name and favorite food on seperate lines of the file make sure the file is closed and run it! You can see the file has been updated with all the new information.
I am going to show you something cool you can do in Python! Because we know that each line only consists of a name and a food, and every line is a different person, this allows us to do something awesome! We can assign a variable to the first word on the line and a variable to the second word on a line in the same statement. Don't forget since we closed the file we need to open the file again but this time for reading. Here is what it will look like:

   food_file = open("Favorite Foods", 'r') #open "Favorite Foods" for reading and assign it to food_file variable 
   for line in food_file: #loop through each line in the food_file
    name, food = line.split(' ',1) #split the line up at the first space, each part gets stored in a different variable
    print(name, "has a favorite food and it's", food)

To break it down these lines of code are going to:

1) loop through each line in the file

2) split up the words in the line into different variables, assigning name to the first word in the line, and food to the second word in the line.

3) Print a new statement with the information from the file

Copy that function into the program and see what the output looks like. 
---
### Step 3 
You may have noticed the **mystery song** file...It's the first part of one of my favorite songs from the year 2013. Except when I was reading in the lyrics from Google I read all the capital letters correctly, but I accidently reversed all the lowercase letters. Instead of using "a", I used "z", and I did this for every letter. This is my favorite song and I may never know the lyrics if you do not help me. 
I know how to change the letter 'z' to 'a' but I need help with the rest of the letters.
    
   mystery_file = open("mystery song", 'r') #Read in the mystery song
   solved_file = open("solved song", 'w') #Create a new file, this will be the translated song 
   for line in mystery_file: #loop through each line in the mystery_file
    for letter in line: #loop through each letter of the given line
     if(letter == 'z'): #if the current letter is lowercase 'z'
     solved_file.write('a') #print current character as 'a' to the solved_file instead of 'z'
     elif().... #next statement for the letter 'y' should be very similar

You are going to have to work with your group to make solving this one easier, split up some of the letters amongst your group. **Remember that I only messed up the lowercase letters, every other letter and space should stay as it is.** 

*Hint: This means that there will probably be a case for "everything **else**" where we just pass on the letter.*
---
**Don't forget to close the file!**

On looking at the final solved output it does look like I messed up another time. I mixed up some of the letters again! I am sure you can figure out what song it is with the mistake, but if anyone in your group likes puzzles then try to code the program to output the correct letters! 

*hint: Figure out which letters were switched with what by guessing what the letter should be!*

**When you figure out the song, make a print statement with the song name and then you are done with the lab!**
