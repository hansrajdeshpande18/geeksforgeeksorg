#if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

a = 330
b = 200

if b >= a:
    print("b is greater than a")
else:
    pass
