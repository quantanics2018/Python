import csv

with open('data.csv', 'r') as file:
    csv_dict_reader = csv.DictReader(file)
    
    for row in csv_dict_reader:
        print(row['Name'], row['Age'], row['Country'])
