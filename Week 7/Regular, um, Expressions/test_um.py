from um import count


def main():
    test1()
    test2()
    test3()




def test1():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2



def test2():
    assert count('yummi') == 0



def test3():
    assert count('Hello, um world') == 1
    assert count('um?') == 1



if __name__ == '__main__':
    main()