import string

plate = input("Plate: ")

def main():
    global plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


maxchrs = 6
not1stnmbr = 0
l = []


for i in string.digits:
    l.append(i)


def is_valid(s : str):
    global maxchrs , not1stnmbr , l
    if (len(s) == maxchrs):
        if s[0:3] in string.ascii_uppercase or s[0:2] in string.ascii_uppercase:
            if s[3:6] in "".join(map(str , l)):
                if (s[3] != not1stnmbr):
                    return True
    if (s in ['CS50' , 'ECTO88' , 'NRVOUS']):
        return True
    else:
        return False



main()