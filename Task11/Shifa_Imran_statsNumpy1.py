import numpy as np
from scipy import stats 

# Creating NumPy arrays 
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Mean
print("\nMean of a:")
print(np.mean(a))

# Median
print("\nMedian of a:")
print(np.median(a))

# Mode
#to implement it we use scipy stats library as numpy doesn't have builtin mode function to calculate directly
print("\nMode of a:")
print(stats.mode(a))

# Variance
print("\nVariance of a:")
print(np.var(a))

# Standard deviation
print("\nStandard deviation of a:")
print(np.std(a))

# Percentile
print("\n75th percentile of a:")
print(np.percentile(a, 75))

# Covariance
print("\nCovariance of b:")
print(np.cov(b))


# Probability Distribution - Normal Distribution
print("\nRandom numbers from Normal Distribution:")
# mean ,standard deviation, size 
print(np.random.normal(0, 1, 5)) 

# Probability Distribution - Binomial Distribution
print("\nRandom numbers from Binomial Distribution:")
# trials, success probability , size 
print(np.random.binomial(7, 0.5, 5)) 

# Probability Distribution - Poisson Distribution
print("\nRandom numbers from Poisson Distribution:")
# lambda, size
print(np.random.poisson(2, 5)) 

