def main():
    greeting = input('Greeting: ')
    valToPrint = value(greeting)
    print(f'${valToPrint}')



def value(greeting):
    greeting = str(greeting).lower().strip()
    if ('hello' in greeting):
        return 0
    elif ('h' == greeting[0]):
        return 20
    else:
        return 100



if __name__ == '__main__':
    main()