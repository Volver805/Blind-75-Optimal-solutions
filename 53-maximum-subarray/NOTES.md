For this problem there's two approaches 
1) Dynamic Programming, Kadane's Algorithm | Log(n)
2) Divide & Conquer 
I'm only going to discuss the dp solution if you want to check the other solution you might refer to this link [Maximum Subarray Sum using Divide and Conquer algorithm
](https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/)
---
## Solution using Dynamic Programming, Kadane's Algorithm | Log(n)
to get the biggest sub-array we actually we want to determine the start and end of a substring.
**notice that when we have element x = 4 and subArrgSum = -2 there is no point of using this sub array anymore as if we start from element x we can achieve to bigger numbers**
thus we determind that the end of the previous sub-array was the element before x and the start of our new subarray is x.
```
  if currNumber > arrSum
    arrSum = sum
    arrSum = currNumber
  else
    arrSum += currNumber
```
```
[-2,1,-3,4,-1,2,1,-5,4]
array          curr     max
[-2]            -2       -2
[1]              1        1
[1,-3]          -2        1 
[4]              4        4 <--- As we find the 4 > 1+(-3) the new sub-array start is [4]
[4,-1            3        4
[4,-1,2]         5        5
[4,-1,2,1]       6        6
[4,-1,2,1,-5]    1        6 <--- There's not point of determining the exact sub array we just need the maxValu that we already have stored
[4,-1,2,1,-5,4]  5        6 
return max
```
