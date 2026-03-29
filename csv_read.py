import csv

# Define the data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Specify the file name
filename = 'data_pipe_delimited.csv'

# Write data to the CSV file with a pipe delimiter
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='|')
    csvwriter.writerows(data)

print(f"Data has been written to {filename}")


# DictWriter

data = [
    {'name': 'Nikhil', 'branch': 'COE', 'year': 2, 'cgpa': 9.0},
    {'name': 'Sanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1},
    {'name': 'Aditya', 'branch': 'IT', 'year': 2, 'cgpa': 9.3},
    {'name': 'Sagar', 'branch': 'SE', 'year': 1, 'cgpa': 9.5},
    {'name': 'Prateek', 'branch': 'MCE', 'year': 3, 'cgpa': 7.8},
    {'name': 'Sahil', 'branch': 'EP', 'year': 2, 'cgpa': 9.1}
]

with open('university_records.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'branch', 'year', 'cgpa']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


with open('Giants.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)


with open('Giants.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines)
