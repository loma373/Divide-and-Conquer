# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:10:52 2021

@author: Amol
"""


def binarySearch(arr, low, high, x): 
    while low <= high: 
  
        mid = low + (high - low) // 2; 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            low = mid + 1
        else: 
            high = mid - 1
    return -1
  
arr = [ 3, 1, 4, 7, 9 ] 
x=int(input('Enter the number you want to search for '))
   
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print ("Element is present at index " + str(result)) 
else: 
    print ("Element is not present in array") 