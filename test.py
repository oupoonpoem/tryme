import csv
with open('sales-cut.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    
    for line in csv_reader:
        print(line)

