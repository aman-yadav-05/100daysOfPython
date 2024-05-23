#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator terminal!")
bill=float(input("Enter the total bill amount: "))
people=int(input("how many people are there?"))
tip=int(input("how much tip you want to give? 10,12 or 15?"))

initial_split=round(bill/people)
tip_amount=(initial_split*(tip/100))
final_split= initial_split+tip_amount
print(f"Each person should pay: {format(final_split,'.2f')}")