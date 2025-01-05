names = input("Give me everybody's names, seperated by a comma. \n").split(",")

import random

print(f"{names[random.randint(0, len(names)-1)]} pays the bill for everyone.")