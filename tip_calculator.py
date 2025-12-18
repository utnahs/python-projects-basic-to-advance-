print("Welcome to the tip calculator")

bill=float(input("What was the total bill? ")) 

tip=float(input("What percentage tip you would like to give, 10,12 or 15 "))

tot=bill*(1+tip/100)

split=float(input("How many people to split the bill? "))

for_each=int(tot/split)

print(f"Each person should pay: {round(for_each,2)}")
