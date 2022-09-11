from project import (__version__ , __name__ , __finalversion__)


def main():
    test_function_1()
    test_function_2()
    test_function_3()


def test_function_1():
    assert __version__ == '2.1.3'


def test_function_2():
    assert __name__ == 'Youtube Downloader'


def test_function_3():
    assert __finalversion__ == False


if (__name__ == '__main__'):
    main()