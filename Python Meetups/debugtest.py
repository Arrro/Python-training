# You can use this if you want to try debugging on your own or to experiment with it more to get a better grasp of how it works!
# If you run the code below obviously there is some mistakes, while the issue might seem fairly easy to find and resolve, you can use some debugging to determine what going where and how its getting there

import csv # Imports csv module to read csv files

def main(): # Defining the main function of the script
    with open(r"C:/Users/ts250078/OneDrive - Teradata/Documents/Git-Repos/Python-training/Python-training/Python Meetups/empFile.csv", newline='') as empData: # Opening the file as a alias
        dataRead = csv.reader(empData) # Places data into a variable for easier readability
        next(dataRead) # Skips header row
        for row in dataRead: # Iterating through the data
            print('Welcome{0}{1} your employee ID is{2}'.format(row[4], row[1], row[3])) # Print the data in a formatted position
    empData.close() # Closes the file to avoid memory/ open file issues

if __name__ == '__main__':
    main() # Calling the main function