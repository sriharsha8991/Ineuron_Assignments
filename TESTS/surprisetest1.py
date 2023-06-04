# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 02:07:58 2023

@author: sriharsha
"""

# =============================EXAM Q1================================================
# Q1: 
    #Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1
# =============================================================================

def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
        


# ==============================EXAM Q2===============================================
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# 
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# 
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# Constraints:
# a. 1 <= s.length <= 10^5
# b. s consists of only lowercase English letters.
# =============================================================================
def firstUniqChar(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    return -1
