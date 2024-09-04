
# with open("weather_data.csv") as weather_data:
#     # for record in weather_data:
#     #     strip_record = record.strip()
#     #     data.append(strip_record)
#     data = weather_data.readlines()
#
# print(data)


# using csv
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) # prints csv object
#     temperatures = []
#     for row in data:
#         # print(row)  # prints each row in data as an array
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# using Pandas
import pandas
weather_data = pandas.read_csv("weather_data.csv")
# print(type(weather_data))   # Type is DataFrame 2d datatype
# print(type(weather_data["temp"]))   # Type is series 1d datatype

# print(weather_data) # prints as rows and columns
# print(weather_data["temp"])

data_dict = weather_data.to_dict()
# print(data_dict)

temp_list = weather_data["temp"].tolist()
# print(temp_list)

# calculate average of temperatures using math
average = sum(temp_list) / len(temp_list)
print(round(average))

# calculate average of temperatures using series in pandas
print(weather_data["temp"].mean())

# Find max value of temperature from the list using pandas series
print(weather_data["temp"].max())

# Pandas converts columns in the csv file as attributes
print(weather_data.condition)

# Get data in a row
print(weather_data[weather_data.day == "Monday"])

# Print the row of data which had the highest temperatures
print(weather_data[weather_data.temp == weather_data.temp.max()])

# Print condition on monday prints condition column value of the row monday
monday = weather_data[weather_data.day == "Monday"]
print(monday.condition)
monday_temp_f = monday.temp[0] * 9/5 + 32
print(monday_temp_f)


# Create a Dataframe from scratch
student_data_dict = {
    "students": ["Kavya", "Sree", "Elsa"],
    "scores": [100, 100, 90]
}
data = pandas.DataFrame(student_data_dict)
print(data)
data.to_csv("student_data")