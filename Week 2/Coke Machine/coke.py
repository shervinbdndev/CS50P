due = 50

while True:
    print(f"Amount Due: {due}")
    temp = int(input('Insert Coin: '))
    if (temp in [50 , 49]):
        continue
    due = due - temp
    if (temp == 30):
        due = 50
        print(f"Change Owed: {due}")
        continue
    if (due < 0):
        print(f"Change Owed: {abs(due)}")
        break
    if (due == 0):
        due = 0
        print(f"Change Owed: {due}")
        break
    continue