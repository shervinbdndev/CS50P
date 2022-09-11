import re
import sys
import inflect
from datetime import date


engine = inflect.engine()


def main():
    birthDate = input('Date of Birth: ')
    try:
        year , month , day = checkBirthday(birthDate)
    except:
        sys.exit('Invalid date')
    dateOfBirth = date(int(year) , int(month) , int(day))
    dateOfToday = date.today()
    diff = dateOfToday - dateOfBirth
    totalMinutes = diff.days * 24 * 60
    output = engine.number_to_words(totalMinutes , andword='')
    print(f"{output.capitalize()} minutes")





def checkBirthday(birthDate:str):
    if (re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}$' , birthDate)):
        year , month , day = birthDate.split(sep='-')
        return year , month , day




if __name__ == "__main__":
    main()