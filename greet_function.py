#Review 
# create a great function and it should contain three print statements and then call the function 

#lets check if we can achieve function overloading in python or not

#function with parameter
def greet_args(name):
    print("hello,",name)
    print(f"How are you doing today,{name}?")
    print("I hope you'll meet some good people today.")

def greet():
    print("hello, this is called without arguments.")

name="aman"
greet()
greet_args("garima")


#function with multiple inputs.
def info(name,age,gender):
    print(f"hello, {name}")
    print(f"You are good to go as you are {age} year old")
    print(f"you'll be give {gender} pronoun.")

# name=input("enter your name: ")
# age=int(input("enter your age: "))
# gender=input("enter you gender: (M/F)")

info(name='ay',age=23,gender='f')


def greet_with(name,location):
    print(f"hello,{name}")
    print(f"what is it like in {location}")


greet_with("aman","janjgir")
greet_with(location="bilaspur",name="anima")
greet_with(location="delhi",name="garima")