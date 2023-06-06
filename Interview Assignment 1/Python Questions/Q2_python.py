# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:25:31 2023

@author: sriharsha
"""

def isValidString(s):
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Find the maximum frequency
    max_freq = max(freq.values())
    
    # Count the number of characters with frequency different from max_freq
    count = sum(1 for f in freq.values() if f != max_freq)
    
    # Check if the string is valid or not
    if count <= 1:
        return "YES"
    else:
        return "NO"
