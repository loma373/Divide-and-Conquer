# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:05:26 2021

@author: Amol
"""


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()

arr = [2,1,11,8,9,0]
print("Given array is ")
printList(arr)
mergeSort(arr)
print("Sorted array is ")
printList(arr)