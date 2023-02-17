# Write your code below this line 👇
print("Welcome to the tip calculator!")
totalVal = float(input("What was the total bill ? $"))
a=10
b=12
c=15
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
totalVal = totalVal + ((tip*totalVal)/100)

members = int(input("How many people to split the bill?"))
print("Each person should pay $"+str(round(totalVal/int(members),2)))