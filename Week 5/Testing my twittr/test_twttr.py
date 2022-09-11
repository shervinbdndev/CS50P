from twttr import shorten


def main():
    testUpperLowerCase()
    testNumbers()
    testPunctuation()


def testUpperLowerCase():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'


def testNumbers():
    assert shorten('1234') == '1234'


def testPunctuation():
    assert shorten('!?.,') == '!?.,'



if __name__ == '__main__':
    main()