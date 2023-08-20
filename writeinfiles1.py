#write line to file 

exmp2 = '/example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

#read file to see if it worked:

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

#write lines to file

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
# Write the strings in the list to text file

with open('/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)