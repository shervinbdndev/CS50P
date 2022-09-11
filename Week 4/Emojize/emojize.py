import emoji

temp = input('Input: ')
em = emoji.emojize(string=temp , language='alias')
print('Output: %s' % em)