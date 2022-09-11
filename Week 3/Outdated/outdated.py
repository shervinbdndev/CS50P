listOfMonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    dateInput: str = input('Date: ')
    if ('/' in dateInput):
        month , day , year = dateInput.split(sep='/')
    elif (',' in dateInput):
        dateInput = dateInput.replace(',' , '')
        month , day , year = dateInput.split(sep=" ")
        if (month in listOfMonths):
            month = listOfMonths.index(month) + 1
            break
    try:
        if (int(month) > 12 or int(day) > 31):
            continue
        else:
            break
    except ValueError:
        continue


print(f"{int(year)}-{int(month):02}-{int(day):02}")