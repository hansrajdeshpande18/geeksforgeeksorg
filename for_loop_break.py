for x in range(200):
    if x == 20: break
    print(x)
else:
    print("Finally Finished..!!")

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)