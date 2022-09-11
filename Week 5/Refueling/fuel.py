def main():
    fraction = input('Fraction: ')
    fractionConverted = convert(fraction)
    output = gauge(fractionConverted)
    print(output)





def convert(fraction):
    while True:
        try:
            numerator , denominator = str(fraction).split(sep='/')
            newNumerator = int(numerator)
            newDenominator = int(denominator)
            f = newNumerator / newDenominator
            if (f <= 1):
                p = int(f * 100)
                return p
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError , ZeroDivisionError):
            raise



def gauge(percentage):
    if (percentage <= 1):
        return 'E'
    elif (percentage >= 90):
        return 'F'
    else:
        return str(percentage) + '%'






if __name__ == '__main__':
    main()