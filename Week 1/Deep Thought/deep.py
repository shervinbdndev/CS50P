temp = input('What is the Answer to the Great Question of Life, the Universe, and Everything?')

if (temp in ['4 2' , '42' , 'FoRty TwO' , 'Forty Two' , 'forty two' , 'Forty-Two' , 'forty-two']):
    print('Yes')
elif (temp in ['50' , 'fifty']):
    print('No')
else:
    print('Yes')