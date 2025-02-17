numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [pow(n, 2) for n in numbers]

even_numbers = [n for n in numbers if n%2 == 0]

print(squared_numbers)
print(even_numbers)

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

common_numbers = [int(n.strip()) for n in file1_data if n in file2_data]

print(common_numbers)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}


print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22, 
    "Sunday": 24
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)