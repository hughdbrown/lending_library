import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Show that the data is dirty
loansData

# Clean the data
loansData.dropna(inplace=True)

column_amt_funded_by_investors = 'Amount.Funded.By.Investors'
column_amt_requested = "Amount.Requested"
column = column_amt_funded_by_investors

# Generate a box plot for the loan amounts 
loansData.boxplot(column=column)
plt.title ("Boxplot of {0} distribution".format(column))
plt.savefig("boxplot.png")
plt.show()

# Generate a histogram for loan amounts
binwidth = 1000
loansData.hist(column=column, bins=np.arange(min(loansData[column]), max(loansData[column]) + binwidth, binwidth))
plt.title("Histogram of {0} frequency".format(column))
plt.savefig("histogram.png")
plt.show()

# Does the data from loan amounts look normally distributed?
import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData[column], dist="norm", plot=plt)
plt.title("QQ of {0} against normal distribution".format(column))
plt.savefig("QQ.png")
plt.show()
