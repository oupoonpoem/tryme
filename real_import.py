import csv
import random
import math
head=[]
data=[]
count=0
with open('sales-try.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:

        count+=1
        if(count==1):
            head.append([row[0],row[6]])
        if(count>1):
            data.append([row[0],row[6]])
        
           

random.shuffle(data)
num=count-1
train_num=math.ceil(0.9*num)
test_num=num-train_num
train=data[:int(train_num)]
#print(head)
#print(train)
print()
test=data[int(train_num):]

head=head.append(test)
print(head)
#print(test)
