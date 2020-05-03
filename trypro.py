import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import csv
import matplotlib.pyplot as plt


with open('sales-cut.csv','r') as csv_file:
    df = csv.reader(csv_file,delimiter='\t')
    
    for line in df:
        print(line[df['category_name']])
    





