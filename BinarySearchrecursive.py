# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:30:37 2021

@author: Amol
"""


def Bsearch_recursive(arr, low, high, key):
    if low==high:
        if arr[low]==key:
            return low
        else:
            return 0
    
    mid=(low+high)//2
    if arr[mid]==key:
        return mid
    
    if key<arr[mid]:
        Bsearch_recursive(arr, low, mid-1, key)
    else:
        Bsearch_recursive(arr, mid+1, high, key)
        

arr=[]
for i in range(10):
    ele=int(input('Enter the element '))
    arr.append(ele)

x=int(input('Enter the number you want to search for '))
   
result = Bsearch_recursive(arr, 0, len(arr)-1, x) 
if result != 0: 
    print ("Element is present at index " + str(result)) 
else: 
    print ("Element is not present in array") 