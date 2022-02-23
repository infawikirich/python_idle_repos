"""
Uses Python's file class to store data to and retrieve data from a text file

"""

def readFileFunc(filename):
    """Print the elements stored in the text file name filename"""

    # Open file to read
    with open(filename, 'r') as readFile:
        for line in readFile:
            print(line)


def writeFileFunc(filename):
    """Allows the user to store data to the text file named filename"""
    with open(filename, 'w') as writeFile:
        
