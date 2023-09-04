import csv

data = [
    ['Name', 'Age', 'Country'],
    ['Alice', 25, 'USA'],
    ['Bob', 30, 'Canada'],
    ['Carol', 22, 'Australia']
]

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write each row of data
    for row in data:
        csv_writer.writerow(row)
