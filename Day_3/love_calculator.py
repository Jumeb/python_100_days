print("Welcome to the Love Calculator!")
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

name = name1.lower() + name2.lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
l = name.count('l')
o = name.count('o')
v = name.count('v')

score = int(str(t + r + u + e) + str(l + o + v + e))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

