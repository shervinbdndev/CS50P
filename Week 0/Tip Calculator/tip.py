dollars = str(input("How much was the meal? "))
percent = str(input("What percentage would you like to tip? "))

sv_d = str(dollars).replace('$' , '');sv_dd : float = float(sv_d)
sv_p = str(percent).replace('%' , '');sv_pp : int = int(sv_p)

tip = (sv_dd * sv_pp) / 100

print(f'Leave ${tip:.2f}')