temp = input('camelCase: ')

def my_func(arg):
    return f"snake_case: {''.join(['_' + str(c).lower() if str(c).isupper() else c for c in arg]).lstrip('_')}"


print(my_func(temp))