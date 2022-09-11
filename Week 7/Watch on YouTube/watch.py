import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if (re.search(r'<iframe(.)*><\/iframe>' , s)):
        pattern = re.search(r'(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)' , s)
        if (pattern):
            splittedURL = pattern.groups()
            return 'https://youtu.be/' + splittedURL[3]




if __name__ == "__main__":
    main()