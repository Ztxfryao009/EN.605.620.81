# partition array to two subsets (disjoint) with minimized sum difference
# Recursive method

import math

# function to find the minimum sum
def minSum (array, i, sum1, sumTotal):
    if i==0:
        return abs((sumTotal-sum1)-sum1);
    else:
        return min(minSum(array, i-1, sum1+array[i-1],sumTotal), minSum(array,i-1, sum1, sumTotal))

def sumTotals (arr, n):
    sumTotal=0
    for i in range (0,n):
        sumTotal =sumTotal + arr[i]
    return minSum(arr, n, 0, sumTotal)

arr=[19,28,26,23,14,6,22,4,12,11,8,1,21,9,13,3]
n=len(arr)
results=sumTotals(arr,n)
print(results)
