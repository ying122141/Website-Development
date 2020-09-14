# Two pointer

Question : https://leetcode.com/problems/trapping-rain-water/

This task can be simplified as finding the concaves in an array. Assuming i being a pointer, the formulation of concave is based on the maximum height of right and left bound on i. The volume of the water can be computed by min(left, high) - arr[i]. With two pointers starting from beginning and end, it would update the maximum height for both sides and computer min(left, high) every round and sum up the water volume.

  - Time Complexity: O(n)

  - Space Complexity: O(n) (input array)
