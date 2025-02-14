import pandas

squirrel_data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv") 


grey_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
red_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

data_dict = {
    "Fur": ['Black', 'Red', 'Grey'],
    "total": [len(black_squirrels), len(red_squirrels), len(grey_squirrels)]
}

data = pandas.DataFrame(data_dict)
data.to_csv('squirrel_count.csv')