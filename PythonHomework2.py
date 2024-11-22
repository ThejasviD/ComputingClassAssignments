# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:44:42 2024

@author: Main
"""

# %%
##Problem 1

import numpy as np

def CountExpClassify(X, G, lam, pi, thresh=0.5):
    K = np.max(G)
    
    # Compute class probabilities for each i in 0, ..., n-1
    prob = (1 - pi) * lam[1] * np.exp(-lam[1] * X) / ((1 - pi) * lam[1] * np.exp(-lam[1] * X) + pi * lam[0] * np.exp(-lam[0] * X))
    
    # Initialize result array of size K + 1
    result = np.zeros(K + 1)
    
    # For each unique value k in G
    for k in range(K + 1):
        # Find indices where G == k
        indices_k = np.where(G == k)[0]
        
        if len(indices_k) > 0:
            # Calculate proportion of probabilities greater than threshold
            result[k] = np.sum(prob[indices_k] > thresh) / len(indices_k)
        else:
            # No indices where G == k, result[k] remains 0
            result[k] = 0
    
    return result

# Example run
X = np.array([1.1, 5.1, 9.1, 4.3, 0.3, 0.8, 1.5])
G = np.array([0, 0, 0, 1, 1, 1, 0])
lam = np.array([0.5, 0.2])
arr = CountExpClassify(X, G, lam, 0.4)
arr

X = np.array([1.1, 5.1, 9.1, 4.3, 0.3, 0.8, 1.5])
G = np.array([0, 0, 0, 1, 1, 1, 0])
G2 = np.array([0, 3, 0, 1, 1, 1, 0])
lam = np.array([0.5, 0.2])
arr1 = CountExpClassify(X, G, lam, 0.6, 0.4)
arr2 = CountExpClassify(X, G, lam, 0.6)
arr3 = CountExpClassify(X, G2, lam, 0.5)
print(arr1)
    #output: [0.5        0.33333333]
print(arr2)
    #output: [0.5 0. ]
print(arr3)
    #output: [0.33333333 0.33333333 0.         1.        ]

# %%
##Problem 2

import pandas as pd
parking = pd.read_csv("C:\\Users\\Main\\Documents\\BST607\\parking_meter.csv")

##Part a
import numpy as np
print( np.median( parking.meter_rate ) )
    #Median meter rate = 2.0
    
condition = (parking.meter_rate < 3) & (parking.time_limit > 8)
print(np.sum(condition))
    #221
    
# %%
    
##Part B
with_credit_card = (parking.credit_card == 'Yes')
without_credit_card = (parking.credit_card == 'No')

print(np.corrcoef(parking.meter_rate[with_credit_card], parking.time_limit[with_credit_card])[0, 1])
    #output: -0.2331505026085801
print(np.corrcoef(parking.meter_rate[without_credit_card], parking.time_limit[without_credit_card])[0, 1])
    #output: -0.05390913939797953
    
# %%

##Part C
print(np.corrcoef(parking.meter_rate[:100], parking.time_limit[:100])[0,1])
    #output: -0.1603935759183292


# %%

##Part D
areas = np.unique(parking.geo_local_area)
NumHighRate = {}
NumHighRate.keys = areas

count_high_rate = np.sum(parking.meter_rate[areas] > 6)
    
    # Mean longitude for the area
mean_longitude = np.mean(longitude[area_mask])
    
    # Add the results to the dictionary
NumHighRate[area] = [count_high_rate, mean_longitude]



# %%

# (d) Create the dictionary
NumHighRate = {}

# Get the unique geographic areas
unique_areas, area_indices = np.unique(parking.geo_local_area, return_inverse=True)

# Loop through each unique geographic area
for i, area in enumerate(unique_areas):
    # Get the indices for the current area
    area_mask = (area_indices == i)
    
    # Number of meters with a rate > 6
    count_high_rate = np.sum(parking.meter_rate[area_mask] > 6)
    
    # Mean longitude for the area
    mean_longitude = np.mean(parking.longitude[area_mask])
    
    # Add the results to the dictionary
    NumHighRate[area] = [count_high_rate, mean_longitude]

print(NumHighRate)
    ##Output:
        ##'Arbutus-Ridge': [np.int64(0), np.float64(-123.15712775421302)], 
        #'Downtown': [np.int64(453), np.float64(-123.11787340444309)], 
        #'Fairview': [np.int64(121), np.float64(-123.13346784560721)], 
        #'Grandview-Woodland': [np.int64(0), np.float64(-123.06886223900176)], 
        #'Hastings-Sunrise': [np.int64(0), np.float64(-123.05524255073628)], 
        #'Kensington-Cedar Cottage': [np.int64(0), np.float64(-123.07102953520976)], 
        #'Kerrisdale': [np.int64(0), np.float64(-123.15691836921523)], 
        #'Killarney': [np.int64(0), np.float64(-123.03414124525193)], 
        #'Kitsilano': [np.int64(0), np.float64(-123.15753318337981)], 
        #'Mount Pleasant': [np.int64(25), np.float64(-123.10592068287289)], 
        #'Renfrew-Collingwood': [np.int64(0), np.float64(-123.03498761940193)], 
        #'Riley Park': [np.int64(0), np.float64(-123.10364946412746)], 
        #'Shaughnessy': [np.int64(0), np.float64(-123.15320234797512)], 
        #'South Cambie': [np.int64(0), np.float64(-123.11604382239572)], 
        #'Strathcona': [np.int64(0), np.float64(-123.0964403153074)],
        #'Sunset': [np.int64(0), np.float64(-123.09080419843164)], 
        #'West End': [np.int64(0), np.float64(-123.13067289967266)],
        #'West Point Grey': [np.int64(0), np.float64(-123.2040283590211)]}












