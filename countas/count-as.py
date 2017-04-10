    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

def count_as(textfile):
    def __init__(self, textfile=""):
        self.textfile = textfile

    def a_counter(self, textfile=""):
        self.my_file = open(self.textfile, "r")
        self.lines = self.my_file.readlines()
        self.a_number = 0
        for line in self.lines:
            oneline = lines[linecount]
            linecount += 1
            halflinelength = len(oneline) // 2
            charcount = 0
            fulltext = ""
            for char in range(halflinelenth):
                fulltext += oneline[charcount]
                charcount += 2


print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
