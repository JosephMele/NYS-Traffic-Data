from matplotlib.pylab import chisquare, norm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm, chisquare, mode

"""
# Question 1
  Does age significantly predict traffic violations among adult male drivers?
  ## Method
    Filter the dataset to include only male drivers 18 or older. Group age ranges and count the violations within each group
  ## Metrics
    - Number of recorded violations by age
    - Percentage of the male-adult ticket sample in each age group
    - Group age differences and fitted trend/model statistics, including a p-value where appropriate
  ## Tools
    Pandas, NumPy, Matplotlib
  ## Plot
    Bar chart of violation counts by age range
"""

#First step, create a dataframe containing only the columns we need
rel_path = "../Data/export.csv"
def plot_from_df(df,num_bins):
    ## Convert the df to list of floats by converting to str, removing commas, and converting to float.
    datalist = df['Age at Violation'].astype(str).str.replace(',', '').astype(float).values
    ##  Use the scipy gamma.fit feature to find the fitted parameters of the distribution.
    fit_shp, fit_loc, fit_scale = gamma.fit(datalist)
    ## Create the bins for the numpy histogram.
    bins = np.r_[np.linspace(18, 100, num_bins), np.inf]    
    ## Find the Median Age
    modeage = mode(datalist)
    fit_mode =  fit_loc + (fit_shp-1)*fit_scale
    percent_error = abs(modeage[0]-fit_mode)/modeage[0]*100
    ## Plot the fitted curve over the matplotlib histogram of the data
    plt.hist(datalist, bins=num_bins, density=True, alpha=0.5, label='Observed Data', edgecolor='k')
    x = np.linspace(min(datalist), max(datalist), 100)
    plt.plot(x, gamma.pdf(x, fit_shp,scale=fit_scale, loc=fit_loc), linewidth=2, color='r', label='Fitted Exponential Distribution')
    plt.title('Comparison of Gamma Model to True Distribution')
    plt.xlabel('Age at Violation')
    plt.ylabel('Counts')
    plt.show()
    return modeage, fit_mode, percent_error

# The pd.read_csv function reads the csv and automatically assigns the header as the specified row.
df = pd.read_csv(rel_path,usecols=[5,6],header=0)
# Index(['Violation Charged Code', 'Violation Description', 'Violation Year',
#  'Violation Month', 'Violation Day of Week', 'Age at Violation',
#  'Gender', 'State of License', 'Police Agency', 'Court', 'Source'],
#  dtype='str')
filtered_df = df[(df['Gender'] == 'M') & (df['Age at Violation'].astype(str).str.replace(',', '').astype(int) >= 18) & (df['Age at Violation'].astype(str).str.replace(',', '').astype(int) <= 100)]
print(f"First five rows:\n{filtered_df.iloc[:5]}\nTotal rows: {len(filtered_df)}")
modeage, fit_modeage, error = plot_from_df(filtered_df,9)
print(f"Most Common Age of Violation:{float(modeage[0])}\n Model Most Common Age of Violation:{float(fit_modeage)}\n Percent Error: {error}%") 

