#ask user number x and y 
x = float(input("What's x? "))
y = float(input("What's y? "))

#adding number and round to bigger side
z = round(x + y)

#formating z to us standart (for example 1,000)
print(f"{z:,}")

