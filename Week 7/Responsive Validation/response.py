from validator_collection import validators


def main():
    emailAddressInput = input("what's your email address? ")
    try:
        emailValidator = validators.email(emailAddressInput)
        print('Valid')
    except:
        print('Invalid')


if __name__ == '__main__':
    main()