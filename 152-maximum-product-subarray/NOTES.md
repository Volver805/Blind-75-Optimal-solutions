This is very similar to  [Maximum Subarray](https://github.com/Volver805/Blind-75-Optimal-solutions/tree/master/53-maximum-subarray) I suggest you go back and solve that problem in case you didn't before attempting to solve this problem
---
In this problem we need to keep an eye for one thing **Negative numbers as they will turn the greatest number into the smallest number but if a the smallest negative number is multipled by another negative number it'll result to the greatest number**
```
4, 5, -3, -1
[4] max = 4, min = 4
[4, 5] max = 20, min = 20
[4, 5, -3] max = 20, min = -60
[4, 5, -3, -1] max = 60, min = -60
````
so unlike maximum subarray where we calculated the maximum sum `currentMaxSum = max(currentMaxSum * nums[i], nums[i])` our maxProduct will be `maxProduct = max(nums[i], maxProduct * nums[i], minProduct * nums[i])` minProduct will be calculated the same but taking the minimum number of the three.
Note : when calculating max and min products store max product in a temporary variable so we can use it when calculating the min product and vice versa.
