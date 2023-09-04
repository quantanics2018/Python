import csv

fieldnames = ['Name', 'Age', 'Country']
data = [
    {'Name': 'Alice', 'Age': 25, 'Country': 'USA'},
    {'Name': 'Bob', 'Age': 30, 'Country': 'Canada'},
    {'Name': 'Carol', 'Age': 22, 'Country': 'Australia'}
]

with open('output.csv', 'w', newline='') as file:
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()  # Write the header row
    
    for row in data:
        csv_dict_writer.writerow(row)
