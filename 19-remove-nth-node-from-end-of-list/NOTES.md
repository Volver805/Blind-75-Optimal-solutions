## one pass approach
we want a to create two node pointers `left` and `right` then we want to have a gab between them exactly equal to `n` so that when we start iterating both of them once right reaches the end left will be exactly before the value that should be deleted.
**Note: when creating the gap if right reaches the end of the list we want to remove the element at beginning so return head.next**
1,2,3,4,5
n = 2
left = 1
right = 1
** lets create our gap**
left = 1
right = 3
** start iterating **
|iteration|left|right|
|---------|----|-----|
|0|1|3|
|1|2|4|
|2|3|5|

left = 3
remove item after left thus remove 4
```output: 1,2,3,5```
