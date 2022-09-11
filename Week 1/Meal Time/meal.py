temp = str(input('What time is it: '))


hours , minutes = temp.split(':')


for i in range(7 , 11 + 1):
    if (hours and minutes == '11'):
        pass
    elif (str(i) == hours):
        print('breakfast time')


for j in range(12 , 17 + 1):
    if (str(j) == hours):
        print('lunch time')


for l in range(18 , 20 + 1):
    if (str(l) == hours):
        print('dinner time')