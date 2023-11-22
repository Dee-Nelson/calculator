weight = int(input("How much do you weigh:  "))
unit = input("(K)g or (L)bs:  ")
kg_to_lbs = weight/0.45
lbs_to_kg = weight * 0.45
if unit.upper() == "K":
    print( f'Your weight in Pounds is: + {kg_to_lbs}')
elif unit.upper() == "L":
    print(f'Your weight in Kilograms is: {lbs_to_kg}')
