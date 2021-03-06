
# - - - - Some code copied from: - - - -
# - 8-9-Best_Fit_Line.py

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

# - - - Variable Index - - - 

# yData: y-coordinates of training data
# xData: x-coordinates of traininf data
# yBestFit: y-coordinates of best fit line
# yPrediction: y-coordinates of prediction
# xToPredict: x-coordinates for predicting yPrediction
# yMean: y-coordinates of mean line of yData
# m: Slope of best fit line
# b: y-intercept of best fit line
# r: Coefficient of determination

# Data
# Need numpy to actually create an array, native python does not have arrays, only lists
xData = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
yData = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

xToPredict = np.array([10,12,7], dtype=np.float64)

# - Formulas used from 7-How_Regression_Works.txt -

# Computing y-intercept b
def intercept(x, y, m):
  b = mean(y) - m * mean(x)
  return b

# Computing slope m
def slope(x, y):
  m = (mean(x) * mean(y) - mean(x * y)) / (mean(x)**2 - mean(x**2))
  return m

# Computing best line fit
def bestFitLine(x, y):
  m = slope(x, y)
  b = intercept(x, y, m)
  return m, b

# - - - - - NEW STUFF FROM TUTORIAL 11 - - - - -

# - Formulas used from 10-R_Squared_Theory.txt -

def coefficientOfDetermination(yOriginal, yBestFit):
  # Calculating y-coordinates for line of mean of all datapoints
  yOriginalMean = [mean(yOriginal) for y in yOriginal]

  # Calculating the difference (error) between best fit line and original datapoints
  squaredErrorBestFit = sum((yBestFit - yOriginal)**2)
  # Calculating the difference (error) between mean line and original datapoints
  squaredErrorOriginal = sum((yOriginalMean - yOriginal)**2)

  # Caluclating coefficient of determination based on above calculations
  r = 1 - (squaredErrorBestFit / squaredErrorOriginal)
  return r, yOriginalMean


# Defining slope m and intercept b
m,b = bestFitLine(xData, yData)

print(f"\nSlope: {m}\ny-Intercept: {b}\n")

# Calculating y-points for regression line
# One line for-loop
yBestFit = [(m*x)+b for x in xData]

# Getting coefficient of determination r as well as mean line of datapoints
r, yMean = coefficientOfDetermination(yData, yBestFit)

print(f"Coefficient Of Determination: {r} -> Higher is Better\n")

# Some simple predictions
yPrediction = [(m*x)+b for x in xToPredict]

# Drawing training data and regression line
plt.scatter(xData, yData)

# Drawing predicted data and regression line
plt.scatter(xToPredict, yPrediction)

# xData provides x-coordinates, regressionLine provides y-coordinates for line a point x
# Plotting without xData would shift line to start from x = 0
# Plotting best fit line
plt.plot(xData, yBestFit)
# Plotting mean line
plt.plot(xData, yMean)
plt.show()
