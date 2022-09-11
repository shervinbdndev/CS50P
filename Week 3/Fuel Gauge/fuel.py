import sys

while True:
    temp = str(input("Fraction: "))
    data = {
        '1/4' : '25%' ,
        '1/2' : '50%' ,
        '3/4' : '75%' ,
        '4/4' : 'F' ,
        '0/4' : 'E'
    }

    maximumhd = 100
    minimumhd = 50
    maximumth = 1000
    minimumth = 500

    try:
        if ('.' in temp or '-' in temp):
            continue

        if (len(temp.split('/')[1]) == len(str(maximumhd))):
            temp2hd : int = int(temp.split('/')[0])
            if (temp2hd > 10 and temp2hd < 50):
                print("25%")
                break
            elif (temp2hd >= 50 and temp2hd < 75):
                print("50%")
                break
            elif (temp2hd >= 75 and temp2hd < 100):
                print("75%")
                break
            elif (int(temp2hd < 10)):
                print("E")
                break
            elif (int(temp2hd >= 90 or temp2hd == maximumhd)):
                print("F")
            else:
                continue
            break

        if (len(temp.split('/')[1]) == len(str(maximumth))):
            temp2th : int = int(temp.split('/')[0])
            if (temp2th > 100 and temp2th < 500):
                print("25%")
                break
            if (temp2th >= 500 and temp2th < 750):
                print("50%")
                break
            if (temp2th >= 750 and temp2th <= 800):
                print("75%")
                break
            if (temp2th < 100):
                print("E")
                break
            if (temp2th >= 900 or temp2th == maximumth):
                print("F")
            else:
                continue
            break

        for i in data.keys():
            if (i in temp):
                print(data[i])
                sys.exit(0)

    except ValueError as VE:
        continue

    except ZeroDivisionError as ZDE:
        continue