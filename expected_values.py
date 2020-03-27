# Script for generating expected values for exponential equation
# And calculating the R^2 value
# Written by: Jennifer Long

import csv
import math

# Constants for regression equation
A = 0.02695
B = 0

# Equation: y = 1-e^(-x)
def get_y(x):
    return 1 - math.exp(-A*(x-B))

# cdf_data_input.txt file contains values [time, probability]
with open('cdf_data_input.txt', encoding='utf16') as csvfile:
    data = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)

    # 1) Find mean of data points
    count, sum = 0, 0
    for row in data:
        time, prob = row
        count += 1
        sum += prob
    mean = sum/count

with open('cdf_data_input.txt', encoding='utf16') as csvfile:
    data = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
    # 2) Squared differences between data points and regression model
    # 3) Squared differences between data points and mean.
    reg_diff_sq, mean_diff_sq = 0, 0
    for row in data:
        time, prob = row
        expected_prob = get_y(float(time))
        # print(time, prob, expected_prob)
        reg_diff_sq += (expected_prob-prob)**2
        mean_diff_sq += (mean-prob)**2

    # 4) Calculating r-squared
    r_squared = 1 - reg_diff_sq/mean_diff_sq
    # print(reg_diff_sq, mean_diff_sq)
    print("R-squared: ", r_squared)
