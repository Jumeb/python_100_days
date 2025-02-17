import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")


{"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

user_name = input("Enter your name: ").upper()

nato_name = [nato_dict[letter] for letter in user_name]

print(nato_name)

