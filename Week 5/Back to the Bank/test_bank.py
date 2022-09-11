from bank import value


def main():
    testReturnZero()
    testReturnTwenty()


def testReturnZero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('HeLlo Gi') == 0


def testReturnTwenty():
    assert value('Hi') == 20
    assert value('hey') == 20

def testReturnHundred():
    assert value("What's up?") == 100
    assert value('good morning') == 100


if __name__ == "__main__":
    main()