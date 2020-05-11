import csv
count=0
with open('sales-cut.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        #print(row[6])
        if (row[6]=='IMPORTED VODKA'):
            count=count+1
print(count)
