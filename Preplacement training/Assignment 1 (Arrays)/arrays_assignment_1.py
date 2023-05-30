# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:12:52 2023

@author: sriharsha
"""

# =============================================================================
# """ Q1:
#     Given an array of integers nums and an integer target, return indices of the two numbers
#  such that they add up to the target 
#  You may assume that each input would have exactly one solution, and you may not use the same element twice
#  You can return the answer in any order
#  Example: 
#      Inputs: nums=[2,7,11,15],target = 9
#      Output:[0,1]
#  """
# =============================================================================


def add_upto_target(nums,target):
     for i in nums:
         if (target-i) in nums:
             return (nums.index(i),nums.index(target-i))
         
 
nums=[22,65,78,2,7,11,15]
target = 9
add_upto_target(nums, target)


# =============================================================================
# """Q2.
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# 
# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# - Return k.
# 
# **Example:**
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# """
# =============================================================================

def rearrange(nums,val):
    count = 0
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i]== val:
            nums[i] = "_"
        else:
            count+=1
      
    return count,nums

nums = [3,2,2,3,3,3,2]
val = 3
print(rearrange(nums, val))
            
            
# =============================================================================
# """
# 
#  **Q3.** Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# **Example 1:**
# Input: nums = [1,3,5,6], target = 5
# 
# Output: 2
# """
# =============================================================================
#Binary Search 
def binarySearch(nums,target):
    "Binary Search Algorithm is used to search an element with logn time complexity"
    start =0
    end = len(nums)-1
    
    while start<=end:
        mid  = start + (end-start)//2
        if target<nums[mid]:
            end = mid-1
        elif target > nums[mid]:
            start = mid+1
        else:
            return mid
    return -1
print(binarySearch([1,3,5,7], 5))


# =============================================================================
# 
# 
#  **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
#  The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of digits.
# 
# **Example 1:**
# Input: digits = [1,2,3]
# Output: [1,2,4]
# 
# **Explanation:** The array represents the integer 123.
# 
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# =============================================================================



def new_int(nums):
    n = ''
    for i in nums:
        n += str(i)
    bn = int(n)+1
    l = []
    while bn>0:
        num = bn%10
        l.append(num)
        bn //=10
    return l[::-1]
print(new_int([8,9,9,9]))




# =============================================================================
# Q5:
#  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 
# **Example 1:**
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# 
# **Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1
# 
# 
# =============================================================================

def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]
    
    
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)


# =============================================================================
# #Q6:
# **Q6.** Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.
# 
# **Example 1:**
# Input: nums = [1,2,3,1]
# 
# Output: true
# =============================================================================

def count_more_than_2(nums):
    for i in nums:
        if nums.count(i)>=2:
            return True
    return False

count_more_than_2([1,2,3,1])


#Q7
# =============================================================================
# **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# **Example 1:**
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# =============================================================================

def shift_zeros_to_end(nums):
    counter =0
    while (0 in nums):
            nums.pop(nums.index(0))
            counter += 1
    for i in range(counter):
        nums.append(0)
    return nums
shift_zeros_to_end([0,1,0,3,12])
    



# =============================================================================
# **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition
# of one number and loss of another number.
# 
# You are given an integer array nums representing the data status of this set after the error.
# 
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# 
# **Example 1:**
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# =============================================================================


def num_check(nums):
    op = list(set([i for i in nums if nums.count(i)==2]))
    for i in range(1,len(nums)):
        if i not in nums:
            op.append(i)
            return op
num_check([1,2,2,4])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

