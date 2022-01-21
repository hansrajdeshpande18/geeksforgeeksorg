#Python conditions and if statements
#equals : a == b
#Not equals : a != b
#Less than : a < b
#Less than or equal too : a <= b
#greater than: a > b
#greater than or equal too : a >= b

x = int(input("Enter value of X:"))
if x > 100:
    print("X is greater than 100")
    if x < 100:
        print("X is smaller than 100")
else:
    print("X is equal to 100")