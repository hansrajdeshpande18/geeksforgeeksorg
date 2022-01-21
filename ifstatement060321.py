name = (input("Enter your name:"))
age = (input("Enter your age:"))
country = (input("Enter your country name:"))

if (age > "70"):
    print(name, " You are eligible for vaccine everywhere")
elif (age > "60") and (country == "India"):
    print(name, "You are eligible for vaccient")
elif ((age > "50") and (country == "UK")):
    print(name, "You are eligible for vaccine")
elif((age < "40") and (country != "UK")):
    print(name, "You are not eligible for vaccine")
elif((age < "40") and (country != "India")):
    print(name, "You are not eligilble for vaccine")
else:
    print(name,"We will email you once you are eligible for vaccine.. Please wait")