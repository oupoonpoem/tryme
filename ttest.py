import numpy as np
import matplotlib.pyplot as mt
from sklearn.svm import SVR
import csv

dates = []
prices = []


def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split("-")[2]))
            prices.append(float(row[1]))
    return


def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    mt.scatter(dates, prices, color='black', label='Data')
    mt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    mt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
    mt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial Model')
    mt.xlabel('Date')
    mt.ylabel('Price')
    mt.title('Support Vector Regression')
    mt.legend()
    mt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


get_data('sales-cut.csv')

predict_price = predict_prices(dates, prices, 50)

print(predict_price)