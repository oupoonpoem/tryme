import csv
with open('sales-cut.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        print(row[0],row[6])

