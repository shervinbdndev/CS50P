data = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "burrito": 7.50,
    "Bowl": 8.50,
    "bowl": 8.50 ,
    "Nachos": 11.00,
    "nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Super quesadilla": 9.50 ,
    "Taco": 3.00,
    "taco": 3.00,
    "Tortilla Salad": 8.00 ,
    "tortilla salad": 8.00
    }

while True:
    try:
        temp1 = str(input("Item: "))
        if (temp1 in data.keys()):
            sv = data[temp1]
            print(f"Total: ${sv:.2f}")
        temp2 = str(input("Item: "))
        if (temp2 in data.keys()):
            sv = data[temp2] + sv
            print(f"Total: ${sv:.2f}")
        temp3 = str(input("Item: "))
        if (temp3 in data.keys()):
            sv = data[temp3] + sv
            print(f"Total: ${sv:.2f}")
    except EOFError:
        break