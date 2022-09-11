import pytest
from fuel import convert , gauge


def main():
    testConvert()
    testGauge()


def testConvert():
    assert convert('1/2') == 50
    assert convert('1/4') == 25
    assert convert('1/100') == 1
    assert convert('99/100') == 99

    with pytest.raises(ValueError):
        convert('cat/dog')

    with pytest.raises(ZeroDivisionError):
        convert('1/0')



def testGauge():
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'



if __name__ == '__main__':
    main()