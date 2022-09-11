temp = str(input("Input: "))


l = []


for i in temp:
    l.append(i)


print(''.join(map(str , l)).replace('i' , '').replace('e' , '').replace('O' , '').replace('o' , '').replace('a' , '').replace('u' , ''))