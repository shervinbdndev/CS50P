from seasons import checkBirthday



def main():
    test1()



def test1():
    assert checkBirthday('1989-05-01') == ('1989' , '05' , '01')
    assert checkBirthday('1989-5-1') == None
    assert checkBirthday('July 3, 1965') == None