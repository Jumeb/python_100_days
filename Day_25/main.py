# with open('weather-data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data)

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# total = 0
# for temp in temp_list:
#     total += int(temp)

average = sum(temp_list) / len(temp_list)

print(average)

print(data["temp"].mean())
print(data["day"].max())

#Get data in row

print(data[data.temp == "Wednesday"]) 
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

mon_temp = int(monday.temp.iloc[0])

mon_temp_fah = mon_temp * 9/5 + 32

print(mon_temp_fah)


#Create a data frame

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")