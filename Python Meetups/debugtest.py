# You can use this if you want to try debugging on your own or to experiment with it more to get a better grasp of how it works!
# If you run the code below obviously there is some mistakes, while the issue might seem obvious, use some debugging to determine what going where and how its getting there

import csv

def main():
    with open(r"C:/Users/ts250078/OneDrive - Teradata/Documents/Git-Repos/Python-training/Python-training/Python Meetups/empFile.csv", newline='') as empData:
        dataRead = csv.reader(empData)
        next(dataRead)
        data = []
        for row in dataRead:
            data.append(row)
            print('Welcome{0}{1} your employee ID is{2}'.format(row[4], row[1], row[3]))
    empData.close()

if __name__ == '__main__':
    main()