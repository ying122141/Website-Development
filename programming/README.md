# Tasks completed

- Dynamic Programming
- Stack, Two pointer
- Data Collection
- Machine Learning

# Task 1 - Dynamic Programming
This task can be simplified as finding the n-subarray within an array which can return a maximal dot product. 

According to rearrangement inequality, the maximal dot product can only be attained by using two sorted arrays with the same order. 

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
This task can be simplified as finding the concaves in an array. Assuming i being a pointer, the formulation of concave is based on the maximum height of right and left bound on i. The volume of the water can be computed by min(left, high) - arr[i]. With two pointers starting from beginning and end, it would update the maximum height for both sides and computer min(left, high) every round and sum up the water volume.

# Task 3 - Data Collection
Web scraping: 

I would use python web libraries and regex to extract text from different mutual fund HTML pages, save and consolidate the data in the pandas dataframe and output to JSON.

APIs:

Depending on the API interface, If it is Python API, I would use pandas dataframe to collect and edit the data and output to JSON format.

# Task 4 - Machine Learning
Google colab link: https://colab.research.google.com/drive/1tiOPorBVebFo5FU4AUKoy01r6Yh8EIQI?usp=sharing

1. What kinds of data pre-processing techniques you have applied in this task? and why?
   
   - Data Imputation: Filling the missing values in dataset
   
   - Data Standardization: When the estimators involve Euclidean distance and the features are in different units, the distance would be misleading and dominate the objective function to produce poor predictions. To achieve better performance, I standardize the data using z = (x - u) / s, where x is a data point, u is mean and s is the standard deviation.
   
2. What kinds of machine learning algorithm you have tried in this task?

   - Support-Vector Machines (SVM) with different kernel tricks
   
3. Which methods perform the best in this task? and why?

   - SVM with RBF kernel. Since the classification is non-linear, the RBF kernel is relatively proper to classify the data by mapping the data into higher dimensions.

4. How would you deal with the lack of training data in this task?

   - Using Leave One Out Cross Validation (LOOCV) to estimate the prediction performance.
   
5. How would you handle an imbalanced dataset in this task?

   - Adjusting the class weight and penalization.
  
6. How would you perform hyperparameter tuning/optimization in this task?

   - Using Grid Search and LOOCV to exhaustively seek optimal parameters.
  
6. How would you evaluate the model in this task?
   
   - Using CV classification accuracy to estimate the model performance.
