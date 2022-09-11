from plates import is_valid


def main():
    testMinMaxChars()
    testStartWithTwoLetters()
    testNumbersInMiddle()
    testNumberZero()
    testPunctuation()



def testMinMaxChars():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFG') == False


def testStartWithTwoLetters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False


def testNumbersInMiddle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False


def testNumberZero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False


def testPunctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI3 14') == False



if __name__ == '__main__':
    main()