temp = str(input("Item: "))

data = {
    "apple":130,
    "banana":110,
    "Avocado":50,
    "Sweet Cherries":100 ,
    "Kiwifruit":90,
    "pear":100
}

if (temp in data.keys()):
    print(f"Calories: {data[temp]}")