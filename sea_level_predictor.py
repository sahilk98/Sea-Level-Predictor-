import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = [df['Year']]; y = [df['CSIRO Adjusted Sea Level']]

    plt.scatter(x,y)

    # Create first line of best fit
    res1 = linregress(x,y) 
    x1 = np.arange(1880,2050)
    y1 = [None]*len(x1)
    for i in range (0,len(x1)):
      y1[i] = (res1.intercept + (res1.slope*x1[i]))
    
    plt.plot(x1, y1, 'r')

    # Create second line of best fit
    df2 = df[120:]
    x2 = [df2['Year']]; y2 = [df2['CSIRO Adjusted Sea Level']]
    plt.scatter(x2,y2)
    res2 = linregress(x2,y2)
    x3 = np.arange(2000,2050)
    y3 = [None]*len(x3)
    for j in range (0,len(x3)):
      y3[j] = (res2.intercept + (res2.slope*x3[j]))
    plt.plot(x3,y3,'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()