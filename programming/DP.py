import numpy as np
import time

def coefficientDP(arr): 

    # Sort the array in descending order
    arr.sort(reverse=True)

    # If the first element is <= 0, maximum value must be 0
    if arr[0] <= 0 : return 0

    # If the first element is > 0, 
    # the current maximum value is the first item of the array
    max_sum = arr[0]
    temp_sum = 0

    m = len(arr)
    
    # Create DP memory matrix
    dp = [[0 for i in range(m)] for j in range(m + 1)]


    # Find the index of the first negative item in the sorted array 
    j = 0
    while j < len(arr) and arr[j] > 0:
        j += 1
    

    # Compute the level of j in  DP memory matrix
    for k in range(1, j+1): 
    
        dp[j][k-1] = (j-k+1) * arr[k-1]
        temp_sum += dp[j][k-1]
    
    if temp_sum > max_sum: 
        max_sum = temp_sum 

    # Find the maximum value value by going through all levels
    for i in range(j+1, m + 1): 
          
        temp_sum = 0
        
        for k in range(0, i): 
            
            dp[i][k] = dp[i-1][k] + arr[k]
            temp_sum += dp[i][k]
       
        
        if temp_sum > max_sum: 
            max_sum = temp_sum 
            
    
    return max_sum


def coefficientShift(arr): 
    
    arr.sort(reverse=True)
    if arr[0] <= 0 : return 0

    j = 0
    while j < len(arr) and arr[j] > 0:
        j += 1
    
    max_sum = arr[0]

    m = len(arr)

    for i in range(j, m + 1): 
          
        temp_sum = 0

        for k in range(1, i+1): 
    
            t = (i-k+1) * arr[k-1]
            temp_sum += t

        if temp_sum > max_sum: 
            max_sum = temp_sum 
            
    return max_sum



if __name__ == '__main__': 

    randnums = np.random.randint(-1000,1000,500).tolist()
    
    
    tStart = time.time()
    print(coefficientDP(randnums))
    tEnd = time.time()
    print(tEnd-tStart)

    tStart = time.time()
    print(coefficientShift(randnums))
    tEnd = time.time()
    print(tEnd-tStart)