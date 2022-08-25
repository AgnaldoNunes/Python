# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()


score1 = name1_lower.count("t") + name2_lower.count("t") + name1_lower.count("r") + name2_lower.count("r") + name1_lower.count("u") + name2_lower.count("u") + name1_lower.count("e") + name2_lower.count("e")

score2 = name1_lower.count("l") + name2_lower.count("l") + name1_lower.count("o") + name2_lower.count("o") + name1_lower.count("v") + name2_lower.count("v") + name1_lower.count("e") + name2_lower.count("e")

scoretotal = int(str(score1) + str(score2))

if scoretotal < 10 or scoretotal > 90:
    print(f"Your score is {scoretotal}, you go together like coke and mentos.")
elif scoretotal >= 40 and scoretotal <= 50:
    print(f"Your score is {scoretotal}, you are alright together.")
else:
    print(f"Your score is {scoretotal}.")