import re


def main():
    print(count(input("Text: ")))


def count(s):
    wordCounter = re.findall(r'\b\W*um\W*' , s , re.IGNORECASE)
    return len(wordCounter)





if __name__ == "__main__":
    main()