#write a program to display current date and time
#datetime module need to import
import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%M-%D \n%H:%M:%S"))