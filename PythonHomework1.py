# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:29:28 2024

@author: Main
"""
###Problem 1
# %%

def KeepLonger(slist, thresh, thresh_vow):
    vowels = ['a', 'e', 'i', 'o', 'u'] 
    result = []  
    
    for s in slist:
        if len(s) > thresh:
            vowel_count = sum(1 for char in s.lower() if char in vowels)
            if vowel_count > thresh_vow:
                result.append(s) 
                
    return result 


x = ["Hello", "World", "Cat", "a", "abcdef"]
print(KeepLonger(x, 3, 1))  
# Output: ["Hello", "abcdef"]

print( KeepLonger(["Hello", "World", "Cat", "a", "abcdef"], 2, 0) )
    #output: ['Hello', 'World', 'Cat', 'abcdef']
    
print( KeepLonger(["", "one", "two", "three"], 3, 1) )
    #output: ['three']
    
print( KeepLonger(["", "one", "two", "three"], 3, 0) )
    #output: ['three']

print( KeepLonger(["", "one", "two", "three"], 5, 1) )
    #output: []

##Problem 2
# %%
def KApprox(a, b, n=100, y0=0.462, z0=0.742):
    # Initialize sequences
    y = [y0]
    z = [z0]

    for _ in range(1, n):
        # Update y
        if y[-1] < 0.517:
            y_next = y[-1] + 0.483
        else:
            y_next = y[-1] - 0.517
        y.append(y_next)

        # Update z
        if z[-1] < 0.517:
            z_next = z[-1] + 0.483
        else:
            z_next = z[-1] - 0.517
        z.append(z_next)

    delta_n = sum(
        abs((1 - (y[k] ** (1 / b))) ** (1 / a) - (1 - (z[k] ** (1 / b))) ** (1 / a))
        for k in range(n)
    ) / n

    return delta_n


print( KApprox(a=5.3, b=1.4, n=5) )
    #output: 0.21030957322576116

print( KApprox(a=1.4, b=5.3, n=5) )
    #output: 0.20259261452718258
    
print( KApprox(a=1.4, b=5.3, n=500) )
    #output: 0.21331297471306634
    
print( KApprox(a=4.1, b=3.5, y0=0.642) )
    #output: 0.10794035938126648

print( KApprox(a=4.1, b=3.5, y0=0.642, z0=0.368) )
    #output: 0.21092729164075824


