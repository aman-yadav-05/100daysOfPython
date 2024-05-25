print("welcome to roller coster ticket counter:")
height=int(input("enter your height in cm:"))

total_bill=0;
if height>=120:
    print("wohooo!!! you can enjoy the ride.")
    age=int(input("enter your age:"))
    if age>=18:
        total_bill=18
        print(f"your ticket price is {total_bill}$")
    elif age<18 and age>12:
        total_bill=12
        print(f"your ticket price is {total_bill}$")
    else:
        total_bill=5
        print(f"your ticket price is {total_bill}$")
else: 
    print("sorry, you need to grow a little taller.")

want_photos=input("do you want photos? Y/N: ")

if want_photos.upper() == 'Y':
    total_bill +=3
    print(f"Your total bill is:{total_bill}")
else:
    print(f"Total bill:{total_bill}")