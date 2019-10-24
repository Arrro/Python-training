# You can use this if you want to try debugging on your own or to experiment with it more to get a better grasp of how it works!
import csv

def main():
    with open(r"C:/Users/ts250078/OneDrive - Teradata/Documents/Git-Repos/Python-training/Python-training/Python Meetups/empFile.csv", newline='') as empData:
        dataRead = csv.reader(empData)
        next(dataRead)
        data = []
        for row in dataRead:
            data.append(row)
    empData.close()

    #print(f'Welcome {fName} {lName} youre Employee ID number is {empId}')

if __name__ == '__main__':
    main()