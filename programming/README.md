# Two pointer
This task can be simplified as finding the concaves in an array. Assuming i being a pointer, the formulation of concave is based on the maximum height of right and left bound on i. The volume of the water can be computed by min(left, high) - arr[i]. With two pointers starting from beginning and end, it would update the maximum height for both sides and computer min(left, high) every round and sum up the water volume.

  - Time Complexity: O(n)

  - Space Complexity: O(n) (input array)


# Machine Learning
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
