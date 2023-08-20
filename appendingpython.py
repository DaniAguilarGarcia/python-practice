# Write a new line to text file

with open('/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")


# Verify if the new line is in the text file

with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())