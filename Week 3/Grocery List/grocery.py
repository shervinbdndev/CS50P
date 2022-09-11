grocery = {}

while True:
    try:
        item = input().lower()
        if (item in grocery):
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key] , str(key).upper())
        break