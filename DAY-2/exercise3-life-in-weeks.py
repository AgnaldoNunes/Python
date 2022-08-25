# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ageleft = 90 - int(age)
days = ageleft*365
weeks = ageleft*52
months = ageleft*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")