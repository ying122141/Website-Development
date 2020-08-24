# Tasks completed

- Dynamic Programming
- Stack, Two pointer
- Data Collection
- Machine Learning

# Task 1 - Dynamic Programming
This task can be simplified as finding the n-subarray within an array which can return a maximal dot product. 

According to Rearrangement inequality, the maximum dot product can only be attained by using two sorted arrays with the same order. 

Example:
```
Input: sorted satisfaction = [3,2,1,-1,-2,-3]

if n = 1
Maximal output for this n: [1] * [3]

if n = 2
Maximal output for this n: [2,1] * [3,2]

if n = 3
Maximal output for this n: [3,2,1] * [3,2,1]

...

if n = 6
Maximal output for this n: [6,5,4,3,2,1] * [3,2,1,-1,-2,-3]
```

Since there is no guaranty that the largest n would give the maximal output, the goal is to try all the possibilities of n. However, if all the items in the array are positive, the maximal dot product must be n = size of an array. As for this, we could try n started from the numbers of positive items til the size of an array. For the above example, we could try n from 3 to 6 so that we could save some computations.

Regarding the algorithm implementation, I have done two versions, which are dynamic programming (DP) and simple nested-for version. Both versions are the same logic but different ways to compute the dot product.

- For the DP, I would add the last level item sum by arr[k], dp[i][k] = dp[i-1][k] + arr[k], where k is pointer looping through the sorted array.

  - Time Complexity: O(n^2)

  - Space Complexity: O(n^2) (DP map)

- For the simple nested-for version, it loops through each n case and uses another for-loop to compute the dot product for each n case.

  - Time Complexity: O(n^2)

  - Space Complexity: O(n) (input array)

Reference of Rearrangement Inequality: https://en.wikipedia.org/wiki/Rearrangement_inequality


# Task 2 - Stack, Two pointer

