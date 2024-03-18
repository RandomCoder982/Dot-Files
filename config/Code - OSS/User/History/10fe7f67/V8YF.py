import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import pandas as pd
import os
from datetime import datetime, timezone
import numpy as np
from scipy import stats
from matplotlib.animation import FuncAnimation

# Load data
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data.csv"))

                
#Applying that function to every value in epoch and creating a new columm containing those values

dates = (mdates.date2num(df["date"]))

debug = True

if debug:
    #Creating the white background
    fig = plt.figure()

    #Creating a 3d graph onto the background
    ax = fig.add_subplot(projection="3d")

    #Graph and labeling the X, Y, and Z lists
    ax.scatter(df["distance"], [*range(len(dates))], dates[::-1])
    ax.set_xlabel('Distance')
    ax.set_ylabel('Calories')
    ax.set_zlabel('Dates')


    ax.zaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #plt.scatter(df["dates"], df["calories"])
    #plt.scatter(df["calories"], df["dates"])
    #plt.scatter([*range(len(df["dates"]))], df["calories"])
    #plt.plot(df["dates"], df["calories"])

plt.show()