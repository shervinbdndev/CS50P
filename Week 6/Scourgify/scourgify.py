import sys
import csv


def main():
    checkCommandLineArgument()
    output = []
    try:
        with open(sys.argv[1] , 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                splitName = row['name'].split(sep=',')
                output.append({'first':splitName[1].lstrip() , 'last':splitName[0] , 'house':row['house']})
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    with open(sys.argv[2] , 'w') as writeFile:
        writer = csv.DictWriter(writeFile , fieldnames=['first' , 'last' , 'house'])
        writer.writerow({'first':'first' , 'last':'last' , 'house':'house'})
        for row in output:
            writer.writerow({'first':row['first'] , 'last':row['last'] , 'house':row['house']})





def checkCommandLineArgument():
    if (len(sys.argv) < 3):
        sys.exit('Too few command-line arguments')
    if (len(sys.argv) > 3):
        sys.exit('Too many command-line arguments')
    if ('.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]):
        sys.exit('Not a CSV file')



if __name__ == '__main__':
    main()