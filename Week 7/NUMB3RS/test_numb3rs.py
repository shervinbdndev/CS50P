from numb3rs import validate


def main():
    testFormat()
    testRange()




def testFormat():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False




def testRange():
    assert validate(r'255.255.255.255') == True
    assert validate(r'1000.255.255.255') == False
    assert validate(r'255.1000.255.255') == False
    assert validate(r'255.255.1000.255') == False
    assert validate(r'255.255.255.1000') == False



if __name__ == '__main__':
    main()