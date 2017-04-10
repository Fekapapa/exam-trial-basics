    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.
from os import path

def count_as(textfile):
    try:
        file_path = path.join('C:\exam-trial-basics\countas', textfile)
        my_file = open(file_path, 'r')
        lines = my_file.readline()
        my_file.close()
        a_number = 0
        for line in lines:
            for letter in line:
                if letter == 'a' or letter == 'A':
                    a_number += 1
        return (a_number)
    except FileNotFoundError:
        return 0


print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
