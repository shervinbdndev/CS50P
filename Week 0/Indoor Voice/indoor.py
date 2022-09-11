temp = input()


def my_func(arg: str):
    inner_arg = arg.lower() if arg.upper() else False
    return inner_arg