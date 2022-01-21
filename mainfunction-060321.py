
#python program to illustrate function with main
def getinteger():
    result = int(input("Enter integer: "))
    return result
def Main():
    print("Started")

    #calling the getinteger function and storing its returned value in the output variable
    output = getinteger()
    print(output)


#now we are required to tell python
#for 'main function existence
if __name__=="__main__":
    Main()