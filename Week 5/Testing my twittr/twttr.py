def main():
    message = input('Input: ')
    msgWvowels = shorten(message)
    print('Output: %s' % msgWvowels)




def shorten(word):
    wWvowels = ''
    for letter in word:
        if (not str(letter).lower() in ['a' , 'i' , 'o' , 'e' , 'u']):
            wWvowels += letter
    return wWvowels



if __name__ == '__main__':
    main()