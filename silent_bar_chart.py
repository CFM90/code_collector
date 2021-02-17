#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:43:40 2021

@author: clemens
"""
#######################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels import datasets
#dir(datasets)

df = datasets.statecrime.load_pandas().data

df["state"] = df.index
df.reset_index(drop =True, inplace = True)

plt.rcParams['figure.dpi']= 300
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams["font.family"] = "Arial"

#######################################################




def visualizer_hbar(units, num_values, interested_unit, skipper, data):
    # create horizontal bar chart for units with no labels except interested_unit
    
    # use skipper to decrease # of units, but make sure interested_unit is included
    df = data.iloc[::skipper,].append(data.loc[data[units] == interested_unit], ignore_index=True)
    df = df.sort_values(num_values,ascending=False)
    df.drop_duplicates(inplace = True)
    df.reset_index(drop =True, inplace = True)

    df["colors"] = np.where(
        df[units] == interested_unit, "red", "grey"
    )

    df.plot.barh(    
        y = num_values,
        x = units,
        color = df.colors.to_list(),
        legend = False,
        width = 1,
        edgecolor = "black",
        linewidth = 0.3
        )

    # edit styles
    plt.title("My Title")
    plt.yticks([])
    plt.xticks([])
    plt.ylabel(units, fontsize = 10, weight='bold')
    plt.xlabel(num_values,fontsize = 10, weight='bold')
    plt.yticks([df[df[units] == interested_unit].index[0]], fontsize = 9)
    #return plt.savefig("Your_path.png", dpi = 300)

    return plt.show()

visualizer_hbar(units = "state", num_values = "murder", interested_unit = "California", skipper= 1, data = df)



    

