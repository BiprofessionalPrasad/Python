# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:48:11 2021

@author: pgaiton


"""

"""
Stationary Time Series
The observations in a stationary time series are not dependent on time.

Time series are stationary if they do not have trend or seasonal effects. Summary statistics calculated on the time series are consistent over time, like the mean or the variance of the observations.

When a time series is stationary, it can be easier to model. Statistical modeling methods assume or require the time series to be stationary to be effective.

Download the the dataset and save it as: daily-total-female-births.csv.
Below is an example of loading the Daily Female Births dataset that is stationary.
"""

from pandas import read_csv
from matplotlib import pyplot
# series = read_csv("daily-total-female-births.csv", header=0, index_col=0)
series = read_csv('K:\Projects\Python programming\daily-total-female-births.csv', header=0, index_col=0)
series.plot()
pyplot.show()

from pandas import read_csv
from matplotlib import pyplot
series = read_csv('daily-total-female-births.csv', header=0, index_col=0)
series.hist()
pyplot.show()


from pandas import read_csv
series = read_csv('daily-total-female-births.csv', header=0, index_col=0)
X = series.values
split = round(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2)) #Running this example shows that the mean and variance values are different, but in the same ball-park

"""
Non-Stationary Time Series
Observations from a non-stationary time series show seasonal effects, trends, and other structures that depend on the time index.

Summary statistics like the mean and variance do change over time, providing a drift in the concepts a model may try to capture.

Classical time series analysis and forecasting methods are concerned with making non-stationary time series data stationary by identifying and removing trends and removing seasonal effects.

Download the dataset and saved it as: international-airline-passengers.csv.
Below is an example of the Airline Passengers dataset that is non-stationary, showing both trend and seasonal components.
"""
from pandas import read_csv
from matplotlib import pyplot
series = read_csv('airline-passengers.csv', header=0, index_col=0)
series.plot()
pyplot.show()


from pandas import read_csv
series = read_csv('airline-passengers.csv', header=0, index_col=0)
X = series.values
split = int(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2)) #Running the example, we can see the mean and variance look very different. We have a non-stationary time series.


from pandas import read_csv
from matplotlib import pyplot
series = read_csv('airline-passengers.csv', header=0, index_col=0)
series.hist()
pyplot.show()


from pandas import read_csv
from matplotlib import pyplot
from numpy import log
series = read_csv('airline-passengers.csv', header=0, index_col=0)
X = series.values
X = log(X)
pyplot.hist(X)
pyplot.show()
pyplot.plot(X)
pyplot.show()


from pandas import read_csv
from matplotlib import pyplot
from numpy import log
series = read_csv('international-airline-passengers.csv', header=0, index_col=0)
X = series.values
X = log(X)
split = round(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))


from pandas import read_csv
from matplotlib import pyplot
from numpy import log
series = read_csv('airline-passengers.csv', header=0, index_col=0)
X = series.values
X = log(X)
split = round(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))

