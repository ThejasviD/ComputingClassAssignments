# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:48:35 2024

@author: Main
"""

# %%

import pandas as pd
ACSFlow = pd.read_csv("C:\\Users\\Main\\Documents\\BST607\\ACSFlow.csv")

# %%
##Problem 1
import numpy as np
print( np.median( ACSFlow.lat2 ) )
    #Output = 41.5490215590779
    
print( np.mean( ACSFlow.lat2 ) )
    #Output = 39.808581370746744

sum(ACSFlow.lat2 < 35)
    #Output = 2604
    
# %%
##Problem 2
ACSFlow['PERC_OUT_TO'] = (ACSFlow.MOVEDOUT / ACSFlow.POP1YR) * 100

sum(ACSFlow.PERC_OUT_TO > 1)
    #Output = 53
    
# %%
##Problem 3
ACSFlow[ACSFlow['POP1YR'] > 100000]['FULL1_NAME'].nunique()
    #Output = 20
    
# %%
#Problem 4
ACSFlow['lat_diff'] = (ACSFlow.lat1 - ACSFlow.lat2)

np.mean(ACSFlow.lat_diff)
    #Output = 3.62379716620342
    
np.corrcoef(ACSFlow.lat_diff,
            ACSFlow.MOVEDNET)[0,1]
     #Output = -0.019736353450866446
    
# %%
##Problem 5
def determine_region(row):
    if row['lat2'] > 38 and row['long2'] > -81:
        return 'Northeast'
    elif row['lat2'] <= 38 and row['long2'] > -98:
        return 'South'
    elif row['lat2'] > 38 and -98 < row['long2'] <= -81:
        return 'Midwest'
    elif -116 < row['long2'] <= -98:
        return 'West'
    elif row['long2'] <= -116:
        return 'Pacific'
    else:
        return 'Unknown'

ACSFlow['Dest_Region'] = ACSFlow.apply(determine_region, axis=1)

print(ACSFlow[['lat2', 'long2', 'Dest_Region']].head())

# %%
##Problem 6

region_moved_out = {
    'Northeast': 0,
    'South': 0,
    'Midwest': 0,
    'West': 0,
    'Pacific': 0
}

for region in region_moved_out.keys():
    region_moved_out[region] = ACSFlow[ACSFlow['Dest_Region'] == region]['MOVEDOUT'].sum()


# %%
##Problem 7
def top_counties_moved_out(reference_county_name):
    filtered_ACS = ACSFlow[ACSFlow['FULL1_NAME'] == reference_county_name]

    top_counties = ACSFlow[ACSFlow['GEOID1'].isin(filtered_ACS['GEOID1'])].nlargest(5, 'MOVEDOUT')

    top_county_names = top_counties['FULL2_NAME'].tolist()

    return top_county_names

top_counties_moved_out('Alcona County, Michigan')

# %%
##Problem 8
filter_ACS = ACSFlow[ACSFlow['PERC_OUT_TO'] > 0.5]

np.corrcoef(filter_ACS.medincome,
            filter_ACS.MOVEDNET)[0,1]
    #Output = 0.15395335047820943

# %%
##Problem 9

unique_medincomes = ACSFlow['medincome'].unique()

percentiles = np.percentile(unique_medincomes, [20, 40, 60, 80])

def assign_incquintile(medincome):
    if medincome <= percentiles[0]:
        return 0
    elif medincome <= percentiles[1]:
        return 1
    elif medincome <= percentiles[2]:
        return 2
    elif medincome <= percentiles[3]:
        return 3
    else:
        return 4

ACSFlow['incquintile'] = ACSFlow['medincome'].apply(assign_incquintile)

sum(ACSFlow.incquintile == 4)
    #Output = 4260
    
# %%
##Problem 10

movement_array = np.zeros((5, 5), dtype=int)

regions = ['Northeast', 'South', 'Midwest', 'West', 'Pacific']

for j in range(5):
    for i, region in enumerate(regions):
        movement_array[j, i] = ACSFlow[(ACSFlow['incquintile'] == j) & (ACSFlow['Dest_Region'] == region)]['MOVEDOUT'].sum()

print(movement_array)
    #output = [[   476   2454  17928    665    169]
              #[  3398  14765  83898   3675   2781]
    #          [  1337   7685  48244   2813    928]
    #          [  2745   9665  77462   4307   2740]
    #          [  9237  27188 186524   8534   9715]]

# %%
##Problem 11
import matplotlib.pyplot as plt
colors = {
    'Northeast': 0,
    'South': 1,
    'Midwest': 2,
    'West': 3,
    'Pacific': 4
}

# Map the Dest_Region to numerical values for coloring
ACSFlow['color'] = ACSFlow['Dest_Region'].map(colors)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x=ACSFlow.MOVEDOUT, y=ACSFlow.lat2, c=ACSFlow.color)
ax.set_xlabel("Moved Out", fontsize=18)
ax.set_ylabel("Latitude 2", fontsize=18)

